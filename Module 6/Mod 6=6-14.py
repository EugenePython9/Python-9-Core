def get_recipe(path, search_id):
    recipe_dict = {'id':'', 'name':'', 'ingredients':[]}
    with open (path, 'r') as opened_file:
        while True:
            line = opened_file.readline()
            if not line:
                return None
            line = line[:-1]
            recipe_line = line.split(',')
            if recipe_line[0] == search_id:
                recipe_dict['id'] = recipe_line[0]
                recipe_dict['name'] = recipe_line[1]
                for ingrid in recipe_line:
                    if ingrid == recipe_dict['id'] or ingrid == recipe_dict['name']:
                        continue
                    recipe_dict['ingredients'].append(ingrid)
                return recipe_dict
            else:
                continue

    