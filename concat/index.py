from multiprocessing.pool import ThreadPool as Pool


def concat(coll, iter):
    if not len(coll):
        return [None, None]
    results = []
    pool = Pool(len(coll))
    try:
        for res in pool.imap(iter, coll):
            print(res)
            results += res
    except Exception as e:
        return [results, e]
    return [results, None]
