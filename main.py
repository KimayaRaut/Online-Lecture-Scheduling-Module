import os
import uvicorn


if __name__ == "__main__":
    # uvicorn.run("v1:app", reload=True, host='0.0.0.0', port=8000, debug=True)
    uvicorn.run("v1:app", reload=True, host='0.0.0.0', port=8000)

