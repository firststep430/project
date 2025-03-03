from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Ingredients, Users

def add_ingredient(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")  # 사용자 ID
        name = request.POST.get("name")  # 재료 이름
        quantity = request.POST.get("quantity")  # 수량

        # 유효성 검사
        if not user_id or not name or not quantity:
            return JsonResponse({"error": "모든 필드를 입력하세요."}, status=400)

        try:
            user = Users.objects.get(id=user_id)  # 해당 유저가 존재하는지 확인
            ingredient = Ingredients(user=user, name=name, quantity=int(quantity))
            ingredient.save()
            return JsonResponse({"success": "재료가 등록되었습니다."})
        except Users.DoesNotExist:
            return JsonResponse({"error": "존재하지 않는 사용자입니다."}, status=400)

    return render(request, "add_ingredient.html")  # GET 요청 시 HTML 렌더링
