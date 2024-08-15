from fasthtml import *
from fasthtml.common import *

# Define team members
team_members = [
    {"name": "Adam Claridge-Chang", "role": "Adam is the originator and lead designer of estimationstats.com and the DABEST/dabestr libraries. He is a neuroscience professor based at Duke-Medical School.", "image": "https://images.ctfassets.net/pcgzt1fmrsri/4EwLpmKTYlnuz6S8agWenO/1bf2eb9b2f529ec15eab1d3253830502/adam.png"},
    # Add more team members as needed
]

def TeamMember(member):
    return Div(
        Div(
            Img(src=member["image"], alt=member["name"]),
            Div(
                H3(member["name"], cls="text-xl font-semibold mt-2"),
                P(
                    Span(member["name"].split()[0], cls="text-blue-600"),
                    " " + " ".join(member["name"].split()[1:]) + " ",
                    member["role"],
                    cls="mt-2 text-gray-600"
                ),
                cls="ml-4 flex-grow"
            ),
            cls="flex items-start"
        ),
        cls="p-6 mb-6"
    )

def meet_the_team():
    return Html(
        Head(
            Title("Meet the Team - Estimation Statistics"),
            Script(src="https://cdn.tailwindcss.com"),
        ),
        Body(
            Div(
                Div(
                    H1("Estimation stats / Meet the team", cls="text-3xl font-bold mb-8 pb-4 border-b"),
                    cls="max-w-4xl mx-auto px-4 py-8"
                ),
                Div(
                    *[TeamMember(member) for member in team_members],
                    cls="max-w-4xl mx-auto px-4"
                ),
                cls="min-h-screen"
            )
        )
    )