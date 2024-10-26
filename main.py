from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from starlette.requests import Request

# Initialize the FastAPI app
app = FastAPI()

# Serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 for rendering HTML templates
templates = Jinja2Templates(directory="templates")

# Define available packages
packages = {
    "Single Class": {"price_per_class": 38},
    "3-Class Pack": {"total_price": 99, "classes": 3},
    "10-Class Pack": {"total_price": 299, "classes": 10},
}

# Define available monthly memberships
monthly_memberships = {
    "4-Class Monthly Membership": {"price": 99, "classes_per_month": 4},
    "8-Class Monthly Membership": {"price": 199, "classes_per_month": 8},
    "12-Class Monthly Membership": {"price": 249, "classes_per_month": 12},
    "Monthly Unlimited Membership": {"price": 299, "classes_per_month": 30},
}

# Route to show the form
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Route to process form submissions
@app.post("/recommend", response_class=HTMLResponse)
async def recommend(request: Request,
                    current_package: str = Form(...),
                    classes_per_month: int = Form(...)):
    # Calculate current monthly cost based on current package
    if current_package == "Single Class":
        current_monthly_cost = classes_per_month * packages["Single Class"]["price_per_class"]
        current_cost_per_class = packages["Single Class"]["price_per_class"]
    else:
        pack_info = packages[current_package]
        pack_price = pack_info["total_price"]
        pack_classes = pack_info["classes"]
        # Calculate how many packs needed to cover classes_per_month
        num_packs = (classes_per_month + pack_classes - 1) // pack_classes  # Ceiling division
        current_monthly_cost = num_packs * pack_price
        current_cost_per_class = current_monthly_cost / classes_per_month

    # Find the best membership option based on classes_per_month
    # Calculate cost for each membership option and choose the one with the lowest total cost
    membership_options = []
    for name, info in monthly_memberships.items():
        if classes_per_month <= info["classes_per_month"]:
            membership_cost = info["price"]
        else:
            # If the membership classes are less than needed, calculate multiple memberships
            num_memberships = (classes_per_month + info["classes_per_month"] - 1) // info["classes_per_month"]
            membership_cost = num_memberships * info["price"]
        membership_options.append((name, membership_cost, info["classes_per_month"]))

    # Choose the membership with the lowest total cost
    best_membership = min(membership_options, key=lambda x: x[1])
    membership_name, membership_total_cost, membership_classes_per_month = best_membership
    membership_cost_per_class = membership_total_cost / classes_per_month

    # Calculate potential savings
    savings = current_monthly_cost - membership_total_cost

    # Determine if the user is saving or spending more
    if savings > 0:
        savings_text = f"You save ${savings:.2f} per month with the membership."
    elif savings < 0:
        savings_text = f"You spend ${-savings:.2f} more per month with the membership."
    else:
        savings_text = "Both options cost the same per month."

    return templates.TemplateResponse("result.html", {
        "request": request,
        "current_package": current_package,
        "current_monthly_cost": f"${current_monthly_cost:.2f}",
        "current_cost_per_class": f"${current_cost_per_class:.2f}",
        "membership_name": membership_name,
        "membership_total_cost": f"${membership_total_cost:.2f}",
        "membership_cost_per_class": f"${membership_cost_per_class:.2f}",
        "savings_text": savings_text,
        "classes_per_month": classes_per_month
    })

# Route to handle POST requests for creating items (Unchanged)
@app.post("/items/")
async def create_item(item: BaseModel):
    item_dict = item.dict()
    if 'tax' in item_dict and item.tax:
        item_dict["price_with_tax"] = item.price + item.tax
    return item_dict


# to open site
# http://127.0.0.1:8000/

# to reload site
# uvicorn main:app --reload

