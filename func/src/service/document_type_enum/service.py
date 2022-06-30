from etria_logger import Gladsheim

from src.core.interfaces.service.document_type_enum.interface import IDocumentTypeEnumService
from src.domain.response.model import ResponseModel
from src.domain.response.status_code.enums import StatusCode
from src.repository.document_type_enum.repository import DocumentTypeEnumRepository


class DocumentTypeEnumService(IDocumentTypeEnumService):
    @classmethod
    def get_response(cls):
        service_response = []

        enums = DocumentTypeEnumRepository.get_document_type_enum()
        for code, value in enums:
            service_response.append({"code": code, "value": value})

        service_response = ResponseModel.build_response(
            success=True, code=StatusCode.SUCCESS, message=None, result=service_response
        )
        return service_response
