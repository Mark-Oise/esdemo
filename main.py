from fasthtml import *
from fasthtml.common import *
from team import meet_the_team 

app = FastHTML()

@app.get("/")
def home():
    return Html(
        Head(
            Title("Estimation Statistics"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Meta(charset="UTF-8"),
            Script(src="https://cdn.tailwindcss.com"),  # Include Tailwind CSS
        ),
        Body(
            Div(
                # Header
                Div(
                    Div(
                        Img(src="https://www.estimationstats.com/static/dist/img/Curve.f6f7c977.svg", alt="Logo", cls=""),
                        cls="flex justify-center ml-16"
                    ),
                    Div(
                        H1("ESTIMATION STATISTICS", cls="text-3xl font-bold"),
                        P("ANALYZE YOUR DATA WITH EFFECT SIZES", cls="text-lg text-gray-600"),
                        cls="max-w-3xl mx-auto px-4"
                    ),
                    cls="py-8"
                ),
                
                # Main content
                Div(
                    # Plot section
                    Div(
                        H2("Plot", cls="inline-block mb-2 text-3xl font-extrabold tracking-tight text-gray-900 dark:text-white"),
                        Hr(cls="h-px my-2 bg-gray-200 border-0 dark:bg-gray-700"),
                        Div(
                            Div(
                                A("Two groups", href="#", cls="text-blue-500"),
                                A("Multiple two-groups", href="#", cls="text-blue-500"),
                                A("Shared control", href="#", cls="text-blue-500"),
                                A("Proportion", href="#", cls="text-blue-500"),
                                A("Delta delta", href="#", cls="text-blue-500"),
                                A("Mini meta", href="#", cls="text-blue-500"),
                                cls="flex flex-col space-y-2"
                            ),
                            Div(
                                A("Paired", href="#", cls="text-blue-500"),
                                A("Multiple paired", href="#", cls="text-blue-500"),
                                A("Repeated measures", href="#", cls="text-blue-500"),
                                A("Proportion paired", href="#", cls="text-blue-500"),
                                A("Delta delta paired", href="#", cls="text-blue-500"),
                                A("Mini meta paired", href="#", cls="text-blue-500"),
                                cls="flex flex-col space-y-2"
                            ),
                            cls="grid grid-cols-2 gap-8"
                        ),
                        cls=""
                    ),
                    
                    # Background section
                    Div(
                        H2("Background", cls="text-2xl font-bold mb-4"),
                        Hr(cls="h-px my-2 bg-gray-200 border-0 dark:bg-gray-700"),
                      
                       Div(
                            Div(
                                A("What is estimation?", href="#", cls="text-blue-500"),
                                A("About this site", href="#", cls="text-blue-500"),
                                A("Meet the team", href="/meet-the-team", cls="text-blue-500"),
                                cls="flex flex-col space-y-2"
                            ),
                            Div(
                                A("Get the code", href="#", cls="text-blue-500"),
                                A("Read the paper", href="#", cls="text-blue-500"),
                                
                                
                                cls="flex flex-col space-y-2"
                            ),
                            cls="grid grid-cols-2 gap-8"
                        ),
                        cls="mt-8"
                    ),
                    
                    # Additional items
                    Div(
                        Div(
                            Img(src="https://www.estimationstats.com/static/dist/img/Box.baa1019b.svg", alt="ESTIMATION STATS", cls=""),
                             Img(src="https://www.estimationstats.com/static/dist/img/DABEST.43a09767.svg", alt="ESTIMATION STATS", cls=""),
                            Img(src="https://www.estimationstats.com/static/dist/img/Box.baa1019b.svg", alt="ESTIMATION STATS", cls=""),
                            Img(src="https://www.estimationstats.com/static/dist/img/Box.baa1019b.svg", alt="ESTIMATION STATS", cls=""),
                           
                            cls="flex items-center space-x-8"
                        ),
                        cls="flex justify-between items-center mt-8 m-8"
                    ),
                    cls="max-w-3xl mx-auto"
                ),
                cls="items-center justify-center container mx-auto px-4"
            )
        )
    )

serve()

@app.get("/meet-the-team")
def team_page():
    return meet_the_team()
