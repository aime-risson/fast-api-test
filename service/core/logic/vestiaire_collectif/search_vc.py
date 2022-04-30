from algoliasearch.search_client import SearchClient
from .from_VC_to_api_data import transform_data_vc
client = SearchClient.create('X1KNQWT5F5', '150bcaf530a12d03415c0cc8ef1267f8')
index = client.init_index('ng-products-master')

def vc_search(search_text="",language='en', price_type='EUR', number_of_items=1, price_from=None, price_to=None):

    numericFilters = []
    if price_from is not None:
        numericFilters.append(f"price.cents.{price_type}>={price_from}")

    if price_to is not None:
        numericFilters.append(f"price.cents.{price_type}<={price_to}")

    search = index.search(search_text,{
    'attributesToRetrieve': [
        "id",
        f"price.cents.{price_type}",
        f"description.searchable.{language}",
        "brand.searchable",
        f"condition.facet.{language}",
        "country",
        f"category.searchable.{language}",
        f"color.searchable.{language}",
        f"name.searchable.{language}",
        f"likes.count",
        "pictures",
        f"link.{language}",
        "seller.id",
        "seller.firstname",
        "creation"

    ],
    'getRankingInfo': True,
    'hitsPerPage': number_of_items,
    "numericFilters" : numericFilters

    })
    # for _item in search["hits"]:
    #     _item.pop('_highlightResult')
    #     _item.pop('_rankingInfo')
    print(search['hits'][0])
    return transform_data_vc(search['hits'])
