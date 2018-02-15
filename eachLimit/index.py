# TODO: reuse code from each
from multiprocessing.pool import ThreadPool as Pool


def each_limit(coll, limit, iter):
    if not len(coll):
        return [None, None]
    if limit < 1:
        return [None, None]
    pool = Pool(min(len(coll), limit))
    try:
        for res in pool.imap_unordered(iter, coll):
            print(res)
            pass
    except Exception as e:
        return [None, e]
    return [None, None]
