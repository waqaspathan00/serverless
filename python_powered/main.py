# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import flask
import requests, json
from util import Response

def get_food(request):
    if request.method == "GET":
        food = request.args["food"]  # get food from url as query param
        if food:
            # perform http get request on api route
            url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey=a8529c104d8749b4a19488d0fd654353&query={food}"
            response = requests.get(url)
            data = json.loads(response.text)
            return Response(data, 200)
        return Response("Must pass query param for food", 400)
    return Response("Invalid request method, use GET", 400)
