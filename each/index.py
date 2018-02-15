from multiprocessing.pool import ThreadPool as Pool

def each(coll, iter):
    pool = Pool(len(coll))
    for res in pool.imap_unordered(iter, coll):
        pass
    return [None, None]
