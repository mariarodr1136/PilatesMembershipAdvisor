from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/recommend", response_class=HTMLResponse)
async def recommend(request: Request, classes_per_month: int = Form(...)):
    # Calculate cost with single classes
    current_package = "Single Class"
    current_monthly_cost = classes_per_month * packages[current_package]["price_per_class"]
    current_cost_per_class = packages[current_package]["price_per_class"]

    # Find the best membership option based on classes_per_month
    best_membership = None
    best_cost = float('inf')
    best_cost_per_class = 0

    # First, filter memberships that can accommodate the requested number of classes
    valid_memberships = {
        name: info for name, info in monthly_memberships.items()
        if info["classes_per_month"] >= classes_per_month or name == "Monthly Unlimited Membership"
    }

    if valid_memberships:
        # Find the cheapest valid membership
        for name, info in valid_memberships.items():
            membership_cost = info["price"]
            cost_per_class = membership_cost / classes_per_month
            
            if membership_cost < best_cost:
                best_cost = membership_cost
                best_membership = name
                best_cost_per_class = cost_per_class
    else:
        # If no single membership can accommodate the classes, calculate multiple memberships
        best_membership = "Multiple Memberships Required"
        
        # Find the most cost-effective combination of memberships
        for name, info in monthly_memberships.items():
            if info["classes_per_month"] > 0:  # Skip unlimited for multiple calculation
                num_memberships = (classes_per_month + info["classes_per_month"] - 1) // info["classes_per_month"]
                total_cost = num_memberships * info["price"]
                
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_membership = f"{num_memberships}x {name}"
                    best_cost_per_class = best_cost / classes_per_month

    # Calculate potential savings
    savings = current_monthly_cost - best_cost

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
        "membership_name": best_membership,
        "membership_total_cost": f"${best_cost:.2f}",
        "membership_cost_per_class": f"${best_cost_per_class:.2f}",
        "savings_text": savings_text,
        "classes_per_month": classes_per_month
    })

# to open site
# http://127.0.0.1:8000/

# to reload site
# uvicorn main:app --reload
