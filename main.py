from reqs import RequestController as req
from db import DBController as database
from utils import UtilController as util
from multiprocessing import Pool
import warnings
import time
import logging

warnings.filterwarnings("ignore", category=UserWarning) 

db = database()

movie_ids = util.load_movie_ids_from_json()
existing = db.get_all_movie_ids()

for m in existing:
    if m in existing:
        movie_ids.remove(m)
logging.info(f"New movies to add: {len(movie_ids)}")

def update_movie_db(movie_id):
    if(db.search_movie_with_index(movie_id) == True ):
        pass
    else:
        url = util.create_api_link(movie_id)
        try:
            time.sleep(.5)
            movie_dict = req.request_movie_from_api(req, url)
            db.insert_movie_from_dict(movie_dict)
            logging.info(f"Added movie: {movie_dict['title']}")
        except:
            time.sleep(.5)
            error_movie_ids.append(movie_id)

def main():
    global error_movie_ids
    error_movie_ids = []
    try:
        pool = Pool(processes=100)
        pool.imap_unordered(update_movie_db, movie_ids)
    except Exception as e:
        logging.warning(f"Updating Error: {e}")
    finally: # To make sure processes are closed in the end, even if errors happen
        pool.close()
        pool.join()
    try:
        pool = Pool(processes=100)
        pool.imap_unordered(update_movie_db, error_movie_ids)
    except Exception as e:
        logging.warning(f"Error List Error: {e}")
    finally: # To make sure processes are closed in the end, even if errors happen
        pool.close()
        pool.join()

if __name__=="__main__":
    main()