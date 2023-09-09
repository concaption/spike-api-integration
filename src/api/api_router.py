"""
API router for the Spike API Integration.
"""

from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi import Request, Form
from src.utils import google_sheets as gs


CLIENT_ID = "your_client_id_here"

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/{user_id}/{provider}")
async def init_integration(user_id: str, provider: str):
    """
    Initializes user integration with a provider.

    Args:
        user_id (str): The ID of the user.
        provider (str): The name of the provider.

    Returns:
        RedirectResponse: A redirect response to the provider with the specified parameters.
    """
    # params = {
    #     "client_id": CLIENT_ID,
    #     "provider": provider,
    #     "user_id": user_id,
    # }

    # integration url
    url = "https://api.spikeapi.com/init-user-integration/"

    # redirect to the provider with the params
    url = f"{url}?provider={provider}&user_id={user_id}&client_id={CLIENT_ID}"
    return RedirectResponse(url=url)


@router.get("/success")
async def success(provider: str, user_id: str, customer_user_id: str):
    """
    Handles successful user integration with a provider.

    Args:
        provider (str): The name of the provider.
        user_id (str): The ID of the user.
        customer_user_id (str): The ID of the customer user.

    Returns:
        RedirectResponse: A redirect response to the return URL.
    """
    temp_dict = {
        "spike_id": user_id,
        "provider": provider,
        "user_id": customer_user_id,
    }
    gs.save_dict_to_sheet("Actual Spike Data", temp_dict)
    return_url = "https://hyperspeed-coaching--ion8.glide.page/"
    return RedirectResponse(url=f"{return_url}")


# @router.route("/authenticate", methods=["GET", "POST"])
# async def authenticate(request: Request):
#     """
#     Displays a form for authenticating with a provider, and handles the form submission.

#     Args:
#         request (Request): The incoming request.

#     Returns:
#         HTMLResponse or RedirectResponse: The HTML response containing the authentication form,
#                           or a redirect response to the provider with the specified parameters.
#     """
#     if request.method == "GET":
#         form_html = """
#             <form method="post" action="/authenticate">
#                <label for="user_id">User ID</label>
#                <input type="text" id="user_id" name="user_id"><br><br>
#                <label for="provider">Provider:</label>
#                <select id="provider" name="provider">
#                     <option value="google_fit">Google Fit</option>
#                     <option value="fitbit">Fitbit</option>
#                     <option value="apple_health">Apple Health</option>
#                 </select><br><br>
#                 <input type="submit" value="Authenticate">
#             </form>
#         """
#         return HTMLResponse(content=form_html, status_code=200)

#     elif request.method == "POST":
#         form = await request.form()
#         user_id = form.get('user_id')
#         provider = form.get('provider')

#         print(f"User ID: {user_id}, Provider: {provider}")
#         url = "https://api.spikeapi.com/init-user-integration/"
#         constructed_url = f"{url}?provider={provider}&user_id={user_id}&client_id={CLIENT_ID}"
#         print(constructed_url)
#         return RedirectResponse(url=constructed_url)


@router.post("/")
async def authenticate(user_id: str = Form(...), provider: str = Form(...)):
    """
    Handles the authentication form submission.
    """
    print(f"User ID: {user_id}, Provider: {provider}")
    return RedirectResponse(url=f"/{user_id}/{provider}", status_code=303)


@router.get("/")
async def authenticate_form(request: Request):
    """
    Displays the authentication form.
    """
    return templates.TemplateResponse("authenticate.html", {"request": request})


# @router.get("/authenticate")
# async def authenticate_form():
#     form_html = """
#         <form method="post" action="/authenticate">
#            <label for="user_id">User ID</label>
#            <input type="text" id="user_id" name="user_id"><br><br>
#            <label for="provider">Provider:</label>
#            <select id="provider" name="provider">
#                 <option value="google_fit">Google Fit</option>
#                 <option value="fitbit">Fitbit</option>
#                 <option value="apple_health">Apple Health</option>
#             </select><br><br>
#             <input type="submit" value="Authenticate">
#         </form>
#     """
#     return HTMLResponse(content=form_html, status_code=200)
