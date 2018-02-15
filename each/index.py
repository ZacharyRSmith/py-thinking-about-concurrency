from multiprocessing.pool import ThreadPool as Pool

def each(coll, iter):
    if not len(coll):
        return [None, None]
    pool = Pool(len(coll))
    for res in pool.imap_unordered(iter, coll):
        pass
    return [None, None]
