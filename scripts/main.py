import uvicorn

from Demo.app import create_app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        use_colors=True,
        host="localhost",
        port=7500,
        reload=True,
    )
