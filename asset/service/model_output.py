def ModelOutput(model, prompt):
    response = model.invoke(prompt).content
    return response