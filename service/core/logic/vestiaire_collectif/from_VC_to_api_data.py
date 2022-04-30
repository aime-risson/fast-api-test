def transform_data_vc(items_data:list, language='en', price_type='EUR'):
    api_data = []
    for _item in items_data:
        data = {}
        data["id"] = _item["id"]
        data['title'] = _item['name']['searchable'][language]
        data["price"] = _item['price']['cents'][price_type] / 100
        data["brand"] = _item['brand']['searchable'][0]
        data["description"] = _item['description']['searchable'][language]
        data["platform"] = "VESTIAIRE_COLLECTIF"
        data["country"] = _item['country']
        data["likes"] = _item['likes']["count"]

        pictures = []
        for picture in _item["pictures"]:
            pictures.append(f"https://images.vestiairecollective.com{picture}")
        data["images"] = pictures

        if language == "en":
            data["link"] = f'https://www.vestiairecollective.com{_item["link"][language]}'
        else:
            data["link"] = f'https://{language}.vestiairecollective.com{_item["link"][language]}'

        data["condition"] = _item["condition"]["facet"][language].split("#")[0]
        data["created_at"] = _item['creation']['date']
        api_data.append(data)

    return {"items":api_data}
