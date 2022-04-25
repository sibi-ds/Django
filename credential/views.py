"""This module is used to call operations on
vaults, components, items and user accesses
"""
import logging

from django.http import HttpRequest

from rest_framework.decorators import api_view
from rest_framework.response import Response

from credential.service import component_service
from credential.service import user_access_service
from credential.service import vault_service

from credential.utils.api_exceptions import CustomApiException


logger = logging.getLogger('credential-manager-logger')


@api_view(['POST'])
def create_vault(request: HttpRequest):
    """Used to create vault
    """
    logger.info(f'Enter {__name__} module, create_vault method')

    try:
        vault = vault_service.create_vault(request.data)
        logger.info(f'Exit {__name__} module, create_vault method')
        return Response(vault)
    except CustomApiException as e:
        logger.error(f'Exit {__name__} module, create_vault method')
        raise CustomApiException(e.status_code, e.detail)


@api_view(['GET', 'PUT', 'PATCH'])
def do_vault(request: HttpRequest, vault_id):
    logger.info(f'Enter {__name__} module, do_vault method')

    if request.method == 'GET':
        try:
            vault = vault_service.get_vault(vault_id, request.data)
            logger.info(f'Exit {__name__} module, do_vault method')
            return Response(vault)
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module, do_vault method')
            raise CustomApiException(e.status_code, e.detail)

    if request.method == 'PUT':
        try:
            vault = vault_service.update_vault(vault_id, request.data)
            logger.info(f'Exit {__name__} module, do_vault method')
            return Response(vault)
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module, do_vault method')
            raise CustomApiException(e.status_code, e.detail)

    if request.method == 'PATCH':
        try:
            vault_active_status = vault_service \
                .change_active_status(vault_id, request.data)
            logger.info(f'Exit {__name__} module, do_vault method')
            return Response(f'Active status changes to {vault_active_status}')
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module, do_vault method')
            raise CustomApiException(e.status_code, e.detail)


@api_view(['POST'])
def create_component(request: HttpRequest, vault_id):
    logger.info(f'Enter {__name__} module, create_component method')

    try:
        component = component_service.create_component(vault_id, request.data)
        logger.info(f'Exit {__name__} module, '
                    f'{create_component.__name__} method')
        return Response(component)
    except CustomApiException as e:
        logger.error(f'Exit {__name__} module, '
                     f'{create_component.__name__} method')
        raise CustomApiException(e.status_code, e.detail)


@api_view(['GET', 'PUT', 'PATCH'])
def do_component(request: HttpRequest, vault_id, component_id):
    logger.info(f'Enter {__name__} module, do_component method')

    if request.method == 'GET':
        try:
            component = component_service.get_component(vault_id, component_id,
                                                        request.data)
            logger.info(f'Exit {__name__} module,'
                        f'{do_component.__name__} method')
            return Response(component)
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module,'
                         f'{do_component.__name__} method')
            raise CustomApiException(e.status_code, e.detail)

    if request.method == 'PUT':
        try:
            component = component_service.update_component(vault_id,
                                                           component_id,
                                                           request.data)
            logger.info(f'Exit {__name__} module, '
                        f'{do_component.__name__} method')
            return Response(component)
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module, '
                         f'{do_component.__name__} method')
            raise CustomApiException(e.status_code, e.detail)

    if request.method == 'PATCH':
        try:
            component_active_status = component_service \
                .change_active_status(vault_id, component_id, request.data)
            logger.info(f'Exit {__name__} module, '
                        f'{do_component.__name__} method')
            return Response(f'Active status changed '
                            f'to {component_active_status}')
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module, '
                         f'{do_component.__name__} method')
            raise CustomApiException(e.status_code, e.detail)


@api_view(['POST', 'PUT', 'PATCH'])
def do_vault_access(request: HttpRequest, vault_id):
    logger.info(f'Enter {__name__} module, do_vault_access method')

    if request.method == 'POST':
        try:
            vault_access = user_access_service \
                .create_vault_access(vault_id, request.data)
            logger.info(f'Exit {__name__} module, '
                        f'{do_vault_access.__name__} method')
            return Response(vault_access)
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module, '
                         f'{do_vault_access.__name__} method')
            raise CustomApiException(e.status_code, e.detail)

    if request.method == 'PATCH':
        try:
            active_status_update_message = user_access_service \
                .remove_vault_access(vault_id, request.data)
            logger.info(f'Exit {__name__} module, '
                         f'{do_vault_access.__name__} method')
            return active_status_update_message
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module, '
                         f'{do_vault_access.__name__} method')
            raise CustomApiException(e.status_code, e.detail)


@api_view(['POST', 'PUT', 'PATCH'])
def do_component_access(request: HttpRequest, vault_id, component_id):
    logger.info(f'Enter {__name__} module, do_component_access method')

    if request.method == 'POST':
        try:
            component_access = user_access_service.create_component_access(
                vault_id, component_id, request.data)
            logger.info(f'Exit {__name__} module, '
                        f'{do_component_access.__name__} method')
            return Response(component_access)
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module, '
                         f'{do_component_access.__name__} method')
            raise CustomApiException(e.status_code, e.detail)

    if request.method == 'PATCH':
        try:
            active_status_update_message = user_access_service \
                .remove_component_access(component_id, request.data)
            logger.info(f'Exit {__name__} module, '
                        f'{do_component_access.__name__} method')
            return active_status_update_message
        except CustomApiException as e:
            logger.error(f'Exit {__name__} module, '
                         f'{do_component_access.__name__} method')
            raise CustomApiException(e.status_code, e.detail)
