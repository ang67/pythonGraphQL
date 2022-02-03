import graphene
import json


class User(graphene.ObjectType):
    id = graphene.ID()
    firstname = graphene.String()
    lastname = graphene.String()
    email = graphene.String()


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(firstname='Bini', lastname='Angui', email='Bini@test.com'),
            User(firstname='Alice', lastname='Yao', email='alice@test.com'),
            User(firstname='Job', lastname='Kouassi', email='job@test.com')
        ][:first]


schema = graphene.Schema(query=Query, auto_camelcase=False)

result = schema.execute(
    '''
    {
        users (first: 4) {
            firstname,
            lastname,
            
        }
    }
    '''
)

items = dict(result.data.items())
print(json.dumps(items, indent=4))
