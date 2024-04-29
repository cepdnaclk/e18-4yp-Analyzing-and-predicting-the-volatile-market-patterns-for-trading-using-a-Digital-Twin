################################### DIGITAL TWIN ######################################

from real_time_run import run
from save_digits import get_last_digits
import asyncio

async def main():
    # Run function_1 and function_2 concurrently
    await asyncio.gather(run(), get_last_digits())

if __name__ == "__main__":

    asyncio.run(main())