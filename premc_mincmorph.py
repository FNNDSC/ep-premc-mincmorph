#!/usr/bin/env python

import os
import sys
from argparse import ArgumentParser, Namespace
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from loguru import logger
from chris_plugin import chris_plugin, PathMapper
from civet.extraction.hemisphere import HemisphereMask
from civet.shells import quiet

parser = ArgumentParser(description='Smoothen masks using mincmorph')
parser.add_argument('-p', '--pattern', default='**/*.mnc',
                    help='pattern for file names to include')
parser.add_argument('-q', '--quiet', action='store_true',
                    help='disable status messages')


def premc_mincmorph(mask: Path, smoothened: Path) -> None:
    HemisphereMask(mask).smoothen_using_mincmorph().save(smoothened, shell=quiet)
    logger.info('Processed {}', smoothened)


@chris_plugin(
    parser=parser,
    category='MRI Processing',
    min_memory_limit='100Mi',
    min_cpu_limit='1000m',
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    if options.quiet:
        logger.remove()
        logger.add(sys.stderr, level='WARNING')

    results = []
    with ThreadPoolExecutor(max_workers=len(os.sched_getaffinity(0))) as pool:
        mapper = PathMapper(inputdir, outputdir, glob=options.pattern, suffix='.mnc')
        for mask, smoothened in mapper:
            results.append(pool.submit(premc_mincmorph, mask, smoothened))

    for future in results:
        e = future.exception()
        if e is not None:
            raise e


if __name__ == '__main__':
    main()
