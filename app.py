import logging
from urllib.parse import urlparse, parse_qs

from quart import request, redirect, Quart


app = Quart(__name__)

@app.route('/', methods=['GET'])
async def handle_request():
    g = ['link', 'utm_source', 'utm_medium', 'utm_campaign', 'datetime']
    parsed_url = urlparse(request.url)
    query_params = parse_qs(parsed_url.query)
    params_list = {i: query_params.get(i, [''])[0] for i in g}
    logging.info(params_list)
    return redirect(params_list['link'])





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
