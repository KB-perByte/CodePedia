import asyncio
import time

async def myWorker(lock, d = "default"):
    print("Attempting to attain lock", d)
    ## acquire lock
    with await lock:
        ## run critical section of code
        print("Currently Locked")
        time.sleep(2)
    ## our worker releases lock at this poit
    print("Unlocked Critical Section")

async def main():
    ## instantiate our lock
    lock = asyncio.Lock()
    ## await the execution of 2 myWorker coroutines
    ## each with our same lock instance passed in
    await asyncio.wait([myWorker(lock, '1'), myWorker(lock, '2')])
    await asyncio.wait([myWorker(lock, '3'), myWorker(lock, '4')])

## Start up a simple loop and run our main function
## until it is complete
lock = asyncio.Lock()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("All Tasks Completed")
loop.close()