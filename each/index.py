from multiprocessing.pool import ThreadPool as Pool

def each(coll, iter):
    if not len(coll):
        return [None, None]
    pool = Pool(len(coll))
    try:
        for res in pool.imap_unordered(iter, coll):
            print(res)
            pass
    except Exception as e:
        return [None, e]
    return [None, None]
