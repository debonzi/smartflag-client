# -*- coding: utf-8 -*-
import smartflags


def test_client_server_endpoint():
    assert smartflags.Client.SF_URL == "https://smartflag.herokuapp.com"