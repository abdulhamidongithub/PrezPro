from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import F

from .models import Fan, CustomUser, Presentation, Darslik, IshReja
from .serializers import (
    FanSerializer,
    UserSerializer,
    PresentationSerializer,
    DarslikSerializer,
    IshRejaSerializer
)

class FanlarAPIView(APIView):
    def get(self, request):
        courses = Fan.objects.all()
        serializer = FanSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data["name"].strip()
        sinf = serializer.validated_data["sinf"]
        guruh = serializer.validated_data["guruh"]
        if Fan.objects.filter(name__iexact=name, sinf=sinf, guruh=guruh).exists():
            return Response(
                {"detail": f"{sinf}-sinf '{name}' fan ({self.guruh} guruh) allaqachon qo'shilgan."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PresentationsAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "fan",
                openapi.IN_QUERY,
                description="Search by subject name. Example: fan=Biology",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "guruh",
                openapi.IN_QUERY,
                description="Guruhi orqali qidirish: guruh=o'zbek / guruh=rus",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "sinf",
                openapi.IN_QUERY,
                description="Filter by class grade (integer). Example: sinf=9",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                "chorak",
                openapi.IN_QUERY,
                description="Filter by chorak (integer). Example: chorak=3",
                type=openapi.TYPE_INTEGER,
            ),
        ]
    )
    def get(self, request):
        filters = {"price": 0}
        fan = request.query_params.get("fan", "").strip()
        if fan:
            filters["darslik__fan__name__iexact"] = fan
        guruh = request.query_params.get("guruh", "").strip()
        if guruh and guruh in ["o'zbek", "rus"]:
            filters["darslik__fan__guruh__iexact"] = guruh
        sinf = request.query_params.get("sinf")
        if sinf and sinf.isdigit():
            filters["darslik__fan__sinf"] = int(sinf)
        chorak = request.query_params.get("chorak")
        if chorak and chorak.isdigit():
            filters["chorak"] = int(chorak)
        presentations = Presentation.objects.filter(**filters)
        serializer = PresentationSerializer(presentations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PresentationAPIView(APIView):
    def get(self, request, pk):
        presentation = get_object_or_404(Presentation, id=pk)
        Presentation.objects.filter(id=pk).update(korishlar_soni=F('korishlar_soni') + 1)
        serializer = PresentationSerializer(presentation)
        return Response(serializer.data)

class DarsliklarAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "fan",
                openapi.IN_QUERY,
                description="Search by subject name. Example: fan=Biology",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "guruh",
                openapi.IN_QUERY,
                description="Guruhi orqali qidirish: guruh=o'zbek / guruh=rus",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "sinf",
                openapi.IN_QUERY,
                description="Filter by class grade (integer). Example: sinf=9",
                type=openapi.TYPE_INTEGER,
            ),
        ]
    )
    def get(self, request):
        filters = {}
        fan = request.query_params.get("fan", "").strip()
        if fan:
            filters["fan__name__iexact"] = fan
        guruh = request.query_params.get("guruh", "").strip()
        if guruh and guruh in ["o'zbek", "rus"]:
            filters["fan__guruh__iexact"] = guruh
        sinf = request.query_params.get("sinf")
        if sinf and sinf.isdigit():
            filters["fan__sinf"] = int(sinf)
        darsliklar = Darslik.objects.filter(**filters)
        serializer = DarslikSerializer(darsliklar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

