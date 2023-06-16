from elasticsearch_dsl import Q


class ElasticQuery:
    @staticmethod
    def generateTermQuery(field, value):
        if value is None:
            return

        query = Q('term', **{field: value})
        return query.to_dict()
