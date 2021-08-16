from flask import Blueprint, render_template,request,abort
from jinja2 import TemplateNotFound
import requests,logging
from os import abort
from dir_api.yandex_api import YandexGeolocationApi
from dir_distance.distance import Distance
from config import yandex_api_key