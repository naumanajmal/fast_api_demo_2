from fastapi import FastAPI, Request, BackgroundTasks
app = FastAPI()


# @app.post("/deploy")
# async def deployProject(request:Request, background_tasks:BackgroundTasks):
#     data = await request.json()
#     repo_url = data["repo_url"]
#     project_name = repo_url.split("/")[-1].replace('.git', '')
#     background_tasks.add_task(clone_and_deploy, repo_url, project_name)
#     return {"status":"deployment started"}

@app.get("/")
async def deployProject():
    
    return {"status":"hello from deployed world"}



