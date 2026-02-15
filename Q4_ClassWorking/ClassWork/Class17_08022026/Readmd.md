# [FastAPI for Agents](https://agentfactory.panaversity.org/docs/Building-Custom-Agents/fastapi-for-agents)
FastAPI for Agents is 40 chapter of Phase 5: Building Custom Agents

## [Build Your FastAPI Skill](https://agentfactory.panaversity.org/docs/Building-Custom-Agents/fastapi-for-agents/build-your-fastapi-skill)
Before learning FastAPI—the Python framework for building production APIs—you'll own a FastAPI skill.

## [POST and Pydantic Models](https://agentfactory.panaversity.org/docs/Building-Custom-Agents/fastapi-for-agents/post-and-pydantic-models)
GET endpoints retrieve data. POST endpoints create data. To create a task, you need to send data in the request body. FastAPI uses Pydantic models to define what that data should look like and validate it automatically.

## [Full CRUD Operations](https://agentfactory.panaversity.org/docs/Building-Custom-Agents/fastapi-for-agents/full-crud-operations)

You've created tasks with POST. Now you complete the picture with Read, Update, and Delete. Together—Create, Read, Update, Delete—these form CRUD, the foundation of data-driven APIs.

## SQL Alchemy ORM (The database toolkit for Python)

SQLAlchemy is a Python library that makes it easier to work with databases. It provides a way to interact with databases using Python code instead of writing raw SQL queries. It is a powerful tool that can be used to build complex database applications.

> We make python object, SQL Alchemy convert it to SQL query and execute it in the database.

Suppose we made class for Pydantic which is doing validation and same class we made again for database which creating table in it. In this case we have same class for two different purposes. But this is **OLD method**, in present days developers merge them and use model called **SQLModel**.

> Pydantic + SQL Alchemy = SQLModel

SQLModel is a library for interacting with SQL databases from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust.

### SQLModel
**SQLModel** is based on Python type annotations, and powered by [Pydantic](https://pydantic-docs.helpmanual.io/) and [SQLAlchemy](https://sqlalchemy.org/).

### [Create a SQLModel Model](https://sqlmodel.tiangolo.com/#create-a-sqlmodel-model)

Then you could create a **SQLModel** model like this:

```python
from sqlmodel import Field, SQLModel

# If table=True, it will work as SQL Alchemy and create a table in the database
# If table=False, it will not create a table in the database and do only validation work of Pydantic
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
```

## [Error Handling](https://agentfactory.panaversity.org/docs/Building-Custom-Agents/fastapi-for-agents/error-handling)

When things go wrong, your API needs to communicate clearly. A missing task should return 404, not crash the server. Invalid input should return 422, not accept garbage. Good error handling makes APIs predictable—and predictability matters enormously for agents.

## [Dependency Injection](https://agentfactory.panaversity.org/docs/Building-Custom-Agents/fastapi-for-agents/dependency-injection)
Every endpoint in your API needs shared resources: configuration, connections, services. You could create these inside each function, but that's repetitive and makes testing hard. Dependency injection solves this—FastAPI creates what your endpoint needs and passes it in.

> Dependency injection is a design pattern where components receive their dependencies from an external source rather than creating them internally. In FastAPI, dependencies are functions that can provide values to endpoints, such as database sessions, authentication credentials, or configuration settings.
