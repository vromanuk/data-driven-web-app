import ssl

import mongoengine


def global_init(user=None, password=None, port=27017,
                server='localhost', use_ssl=True, db_name='pypi'):
    if user or password:
        data = dict(
            username=dict,
            password=password,
            host=server,
            port=port,
            authentication_source='admin',
            authentication_mechanism='SCRAM-SHA-1',
            ssl=use_ssl,
            ssl_cert_reqs=ssl.CERT_NONE
        )
        mongoengine.register_connection(alias='core', name=db_name, **data)
        data['password'] = '*' * 10
        print(f'--> Registering prod connection: {data}')
    else:
        print('--> Registering dev connection')
        mongoengine.register_connection(alias='core', name=db_name)
