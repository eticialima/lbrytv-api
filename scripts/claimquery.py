from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import re

# Reconhece o link na string e retorna o link


def convert_to_stringlink(description):

    desc = (re.sub(r'(http\S+)', r"<a target='_blank' href='\1'>\1</a>", description))

    return desc.replace("\n", " <br> ")


def get_video_in_playlist(claim_id_list):
    query = "select * from claim where claim_id in '{}'+ORDER+BY+release_time+DESC+LIMIT+100".format(
        claim_id_list).replace(" ", "+")

    url = "https://chainquery.lbry.com/api/sql?query={}".format(query)

    data = requests.get(url).json()

    return [el for el in data['data']]


def VideoDetalhes(request, claim_id):
    print(claim_id)  # show id of playlist

    query = "select * from claim where claim_id = '{}'+and+type='claimlist'+ORDER+BY+release_time+DESC+LIMIT+100".format(
        claim_id).replace(" ", "+")

    url = "https://chainquery.lbry.com/api/sql?query={}".format(query)

    data = requests.get(url).json()

    print(url)

    claim_id_list = [el['claim_id_list'] for el in data['data']][0]

    print(claim_id_list)  # show id of playlist

    pass
    # context = [{
    #     'claim_id': el['claim_id']
    # } for el in result][0]

    # return render(request, 'detalhes.html', context)
