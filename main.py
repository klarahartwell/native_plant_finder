from drafter import *
from dataclasses import dataclass

#dataclasses
@dataclass
class Plant:
    name: str
    native_regions: list[int]
    sun: str
    mature_size_sqft: float
    difficulty: str
    bloom_months: list[int]
    #image: str

@dataclass
class State:
    location: str
    gardening_level: str
    space_sqft: int
    recommended_plants: list[Plant]
    saved_plants: list[Plant]

#plant data
ALL_PLANTS = [
    Plant("Sweet Pepperbush", [63, 84], "Full sun to full shade", 8, "beginner", [7, 9]),
    Plant("Inkberry Holly", [63, 84], "Full sun to partial shade", 8, "beginner", [5, 6]),
    Plant("Highbush Blueberry", [63, 84], "Full sun to partial shade", 12, "intermediate", [4, 5]),
    Plant("Bayberry", [63, 84], "Full sun to partial shade", 10, "beginner", [4, 5]),
    Plant("Swamp Rose", [63, 84], "Full sun to partial shade", 6, "intermediate", [6, 8]),
    Plant("Swamp Milkweed", [63, 84], "Full sun to partial shade", 5, "beginner", [6, 8]),
    Plant("Seaside Goldenrod", [63, 84], "Full sun", 6, "beginner", [8, 10]),
    Plant("Butterfly Weed", [63, 84, 67], "Full sun", 2, "beginner", [6, 8]),
    Plant("Blue Flag Iris", [63, 84], "Full sun to partial shade", 3, "intermediate", [5, 7]),
    Plant("Switchgrass", [63, 84], "Full sun", 6, "beginner", [7, 10]),
    Plant("Pink Muhly Grass", [63, 84], "Full sun", 3, "beginner", [9, 11]),
    Plant("Little Bluestem", [63, 84], "Full sun", 4, "beginner", [8, 10]),
    Plant("Cinnamon Fern", [63, 84], "Partial shade to full shade", 3, "intermediate", []),
    Plant("Coastal Plain Bushy St. John's Wort", [63, 84], "Full sun to partial shade", 5, "beginner", [7, 9]),
    Plant("Buttonbush", [63, 84], "Full sun to partial shade", 10, "beginner", [6, 8]),
    Plant("Winterberry", [63, 84], "Full sun to partial shade", 10, "beginner", [6, 7]),
    Plant("Black Huckleberry", [63, 84], "Full sun to partial shade", 3, "intermediate", [5, 6]),
    Plant("Coastal Plain Joe-Pye Weed", [63, 84], "Full sun to partial shade", 5, "beginner", [7, 9]),
    Plant("Wild Bergamot", [63, 84], "Full sun to partial shade", 4, "beginner", [6, 8]),
    Plant("Narrow-Leaved Mountain Mint", [63, 84], "Full sun to partial shade", 3, "beginner", [6, 8]),
    Plant("Cardinal Flower", [63, 84], "Full sun to partial shade", 4, "intermediate", [7, 9]),
    Plant("Broomsedge Bluestem", [63, 84], "Full sun", 4, "beginner", [9, 11]),
    Plant("Coastal Panicgrass", [63, 84], "Full sun", 6, "beginner", [8, 10]),
    Plant("Netted Chain Fern", [63, 84], "Partial shade to full shade", 2, "intermediate", []),
    Plant("Northern Spicebush", [64], "Partial shade to full shade", 10, "beginner", [3, 4]),
    Plant("Mapleleaf Viburnum", [64], "Partial shade to full shade", 6, "beginner", [5, 6]),
    Plant("New Jersey Tea", [64], "Full sun to partial shade", 3, "beginner", [5, 7]),
    Plant("Hearts-a-Bustin", [64], "Partial shade to full shade", 10, "intermediate", [5, 6]),
    Plant("White Wood Aster", [64], "Partial shade to full shade", 3, "beginner", [8, 10]),
    Plant("Wild Geranium", [64], "Partial shade to full shade", 2, "beginner", [4, 6]),
    Plant("Virginia Bluebells", [64], "Partial shade to full shade", 2, "intermediate", [3, 5]),
    Plant("Black-Eyed Susan", [64], "Full sun to partial shade", 3, "beginner", [6, 9]),
    Plant("Foamflower", [64], "Partial shade to full shade", 1, "beginner", [4, 5]),
    Plant("Pennsylvania Sedge", [64], "Partial shade to full shade", 1, "beginner", [4, 5]),
    Plant("Bottlebrush Grass", [64], "Partial shade to full shade", 4, "beginner", [6, 8]),
    Plant("Christmas Fern", [64], "Partial shade to full shade", 2, "beginner", []),
    Plant("Maidenhair Fern", [64], "Partial shade to full shade", 2, "intermediate", []),
    Plant("Mountain Laurel", [58], "Partial shade to full shade", 10, "intermediate", [5, 6]),
    Plant("Witch Hazel", [58], "Full sun to partial shade", 15, "beginner", [10, 12]),
    Plant("Lowbush Blueberry", [58], "Full sun to partial shade", 2, "intermediate", [5, 6]),
    Plant("Purple-Flowering Raspberry", [58], "Partial shade to full shade", 6, "beginner", [6, 8]),
    Plant("Wild Columbine", [58], "Partial shade to full shade", 3, "beginner", [4, 6]),
    Plant("Sharp-Lobed Hepatica", [58], "Partial shade to full shade", 1, "advanced", [3, 4]),
    Plant("Red Trillium", [58], "Partial shade to full shade", 1, "intermediate", [4, 5]),
    Plant("Zigzag Goldenrod", [58], "Partial shade to full shade", 3, "beginner", [7, 9]),
    Plant("Marginal Wood Fern", [58], "Partial shade to full shade", 2, "beginner", []),
    Plant("Rock Polypody", [58], "Partial shade to full shade", 1, "intermediate", []),
    Plant("Pennsylvania Sedge", [58], "Partial shade to full shade", 1, "beginner", [4, 5]),
    Plant("Fragrant Sumac", [67], "Full sun to partial shade", 6, "beginner", [3, 4]),
    Plant("American Hazelnut", [67], "Full sun to partial shade", 15, "beginner", [2, 4]),
    Plant("Ninebark", [67], "Full sun to partial shade", 10, "beginner", [5, 7]),
    Plant("Silky Dogwood", [67], "Full sun to partial shade", 12, "beginner", [5, 6]),
    Plant("Butterfly Milkweed", [67], "Full sun", 2, "beginner", [6, 8]),
    Plant("Wild Blue Phlox", [67], "Partial shade to full shade", 2, "beginner", [4, 5]),
    Plant("Smooth Blue Aster", [67], "Full sun to partial shade", 4, "beginner", [8, 10]),
    Plant("Nodding Onion", [67], "Full sun to partial shade", 1, "beginner", [6, 8]),
    Plant("Big Bluestem", [67], "Full sun", 8, "beginner", [8, 10]),
    Plant("Indian Grass", [67], "Full sun", 8, "beginner", [8, 10]),
    Plant("Interrupted Fern", [67], "Partial shade to full shade", 3, "beginner", []),
    Plant("Rhodora", [60, 62], "Full sun to partial shade", 3, "intermediate", [4, 5]),
    Plant("Sheep Laurel", [60, 62], "Partial shade to full shade", 3, "advanced", [5, 7]),
    Plant("Speckled Alder", [60, 62], "Full sun to partial shade", 15, "intermediate", [3, 4]),
    Plant("Winterberry", [60, 62], "Full sun to partial shade", 10, "beginner", [6, 7]),
    Plant("Bunchberry", [60, 62], "Partial shade to full shade", 1, "advanced", [5, 7]),
    Plant("Painted Trillium", [60, 62], "Partial shade to full shade", 1, "advanced", [4, 6]),
    Plant("Goldthread", [60, 62], "Partial shade to full shade", 0.5, "advanced", [4, 6]),
    Plant("Bluebead Lily", [60, 62], "Partial shade to full shade", 2, "intermediate", [5, 6]),
    Plant("Ostrich Fern", [60, 62], "Partial shade to full shade", 5, "beginner", []),
    Plant("Hay-Scented Fern", [60, 62], "Partial shade to full shade", 2.5, "beginner", []),
    Plant("Tussock Sedge", [60, 62], "Full sun to partial shade", 3, "intermediate", [5, 7]),
    Plant("Rosebay Rhododendron", [69, 70], "Partial shade to full shade", 20, "intermediate", [6, 7]),
    Plant("Wild Hydrangea", [69, 70], "Partial shade to full shade", 5, "beginner", [6, 8]),
    Plant("Bush Honeysuckle", [69, 70], "Full sun to partial shade", 4, "beginner", [5, 7]),
    Plant("Bladdernut", [69, 70], "Partial shade to full shade", 15, "intermediate", [4, 5]),
    Plant("Large-Flowered Trillium", [69, 70], "Partial shade to full shade", 1.5, "intermediate", [4, 5]),
    Plant("Blue Cohosh", [69, 70], "Partial shade to full shade", 3, "advanced", [4, 5]),
    Plant("Blue Mistflower", [69, 70], "Full sun to partial shade", 3, "beginner", [7, 9]),
    Plant("Virginia Strawberry", [69, 70], "Full sun to partial shade", 0.7, "beginner", [4, 6]),
    Plant("River Oats", [69, 70], "Partial shade to full shade", 4, "beginner", [7, 9]),
    Plant("New York Fern", [69, 70], "Partial shade to full shade", 3, "beginner", []),
    Plant("Sensitive Fern", [69, 70], "Partial shade to full shade", 3, "beginner", []),
    ]
    
LEVELS = ["beginner", "intermediate", "advanced", "expert"]

MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

#routes
@route
def index(state: State) -> Page:
    return Page(state, [
        "Native Plant Finder",
        LineBreak(),
        "Find native plants for your garden in DE, NJ, and PA.",
        LineBreak(),
        Button("Get started", location_page),
        Button("What are native plants?", about_page),
    ])

@route
def about_page(state: State) -> Page:
    return Page(state, [
        "What are native plants?",
        LineBreak(),
        "Native plants are plants that grew in this region before European settlement. "
        "Local insects and birds evolved alongside them, so they support more "
        "wildlife and usually need less watering than non-native plants.",
        LineBreak(), LineBreak(),
        "Plant data/Sources: ",
        LineBreak(),
        "- bplant.org. \"Ecoregions of North America.\" https://bplant.org/regions.php. Accessed November 2026.",
        LineBreak(),
        "- U.S. Environmental Protection Agency. \"Level III and IV Ecoregions of the Continental United States.\" https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Accessed November 2026.",
        LineBreak(),
        Button("Back to home", index),
    ])

@route
def start_over(state: State) -> Page:
    state.location = ""
    state.gardening_level = "beginner"
    state.space_sqft = 0
    state.recommended_plants = []
    state.saved_plants = []
    return index(state)

@route
def set_location(state: State, location: str) -> Page:
    state.location = location
    return preferences_page(state)

@route
def location_page(state: State) -> Page:
    return Page(state, [
        "Where is your garden?",
        LineBreak(),
        "Find your area on the map, then pick its region number below.",
        LineBreak(),
        Image("ecoregions.png", width=450),
        LineBreak(),
        SelectBox("location", ["58", "60", "62", "63", "64", "67", "69", "70", "84"], state.location),
        Button("Next", set_location),
    ])

@route
def preferences_page(state: State) -> Page:
    return Page(state, [
        "What is your gardening level?",
        LineBreak(),
        "Beginner: I'm new to gardening and want easy plants.",
        Button("Beginner", pick_beginner),
        LineBreak(),
        "Intermediate: I've grown some plants and can handle a bit more care.",
        Button("Intermediate", pick_intermediate),
        LineBreak(),
        "Advanced: I'm comfortable with soil, pruning, and seasonal care.",
        Button("Advanced", pick_advanced),
        LineBreak(),
        "Expert: I want challenging or specialized plants.",
        Button("Expert", pick_expert),
    ])

@route
def pick_beginner(state: State) -> Page:
    state.gardening_level = "beginner"
    return space_page(state)

@route
def pick_intermediate(state: State) -> Page:
    state.gardening_level = "intermediate"
    return space_page(state)

@route
def pick_advanced(state: State) -> Page:
    state.gardening_level = "advanced"
    return space_page(state)

@route
def pick_expert(state: State) -> Page:
    state.gardening_level = "expert"
    return space_page(state)

@route
def set_space(state: State, space: str) -> Page:
    if not space.isdigit():
        return Page(state, [
            "Please enter a whole number, like 50.",
            LineBreak(),
            "Enter the area in square feet.",
            TextBox("space", ""),
            Button("Next", set_space),
        ])
    if int(space) <= 0:
        return Page(state, [
            "Your space needs to be greater than 0.",
            LineBreak(),
            "Enter the area in square feet.",
            TextBox("space", ""),
            Button("Next", set_space),
        ])
    state.space_sqft = int(space)
    state.recommended_plants = []
    region = int(state.location)
    for plant in ALL_PLANTS:
        if (region in plant.native_regions
                and plant.mature_size_sqft <= state.space_sqft
                and LEVELS.index(plant.difficulty) <= LEVELS.index(state.gardening_level)):
            state.recommended_plants.append(plant)
    return results_page(state)

@route
def space_page(state: State) -> Page:
    return Page(state, [
        "How much garden space do you have?",
        LineBreak(),
        "Enter the area in square feet (for example, 50). A visual is below to help you estimate how much space you have.",
        LineBreak(),
        Image("sq_ft_visual.png", width=450),
        LineBreak(),
        TextBox("space", ""),
        Button("Next", set_space),
    ])

@route
def results_page(state: State) -> Page:
    content = ["Plants for you -- Name | Sun | Mature Size | Bloom Months:", LineBreak(), LineBreak()]
    if len(state.recommended_plants) == 0:
        content.append("No matches. Try a larger space or a different region.")
    else:
        for plant in state.recommended_plants:
            content.append(plant.name + " | " + plant.sun + " | " + str(plant.mature_size_sqft) + " sq ft" + " | ")
            if len(plant.bloom_months) == 2:
                content.append("Blooms: months " + str(plant.bloom_months[0]) + " to " + str(plant.bloom_months[1]))
            else:
                content.append("Foliage only")
            content.append(LineBreak())
        content.append("Pick a plant to save:")
        content.append(SelectBox("plant_name",
                                 [p.name for p in state.recommended_plants],
                                 state.recommended_plants[0].name))
        content.append(Button("Save plant", save_plant))
        content.append(LineBreak())
        content.append("Saved so far: " + str(len(state.saved_plants)))
        content.append(Button("View my garden plan", plan_page))
        content.append(LineBreak())
        content.append(Button("Start over", start_over))
    return Page(state, content)

@route
def save_plant(state: State, plant_name: str) -> Page:
    for plant in state.recommended_plants:
        if plant.name == plant_name:
            already_saved = False
            for saved in state.saved_plants:
                if saved.name == plant_name:
                    already_saved = True
            if not already_saved:
                state.saved_plants.append(plant)
    return results_page(state)

@route
def plan_page(state: State) -> Page:
    content = ["My Garden Plan:", LineBreak(), "We check March through November, when most pollinators are active.", LineBreak(), LineBreak()]
    if len(state.saved_plants) == 0:
        content.append("You haven't saved any plants yet.")
    else:
        months_covered = []
        total_space = 0
        for plant in state.saved_plants:
            total_space += plant.mature_size_sqft
            if len(plant.bloom_months) == 2:
                content.append(plant.name + " blooms "
                               + MONTH_NAMES[plant.bloom_months[0] - 1] + " to "
                               + MONTH_NAMES[plant.bloom_months[1] - 1])
                for month in range(plant.bloom_months[0], plant.bloom_months[1] + 1):
                    if month not in months_covered:
                        months_covered.append(month)
            else:
                content.append(plant.name + " (foliage only)")
            content.append(LineBreak())

        content.append("Space used: " + str(total_space) + " of " + str(state.space_sqft) + " sq ft")
        if total_space > state.space_sqft:
            content.append("Your plan is bigger than your garden. Consider removing a plant.")
        content.append(LineBreak())
        missing = []
        for month in range(3, 12):
            if month not in months_covered:
                missing.append(MONTH_NAMES[month - 1])
        if len(missing) == 0:
            content.append("Something in your garden blooms every month from March to November.")
        else:
            content.append("No blooms in: " + ", ".join(missing))
        content.append(LineBreak())
        content.append("Pick a plant to remove:")
        content.append(SelectBox("plant_name",
                                 [p.name for p in state.saved_plants],
                                 state.saved_plants[0].name))
        content.append(Button("Remove plant", remove_plant))
    content.append(LineBreak())
    content.append(Button("Back to results", results_page))
    content.append(Button("Start over", start_over))
    return Page(state, content)

@route
def remove_plant(state: State, plant_name: str) -> Page:
    kept = []
    for plant in state.saved_plants:
        if plant.name != plant_name:
            kept.append(plant)
    state.saved_plants = kept
    return plan_page(state)

@route
def start_over(state: State) -> Page:
    state.location = ""
    state.gardening_level = "beginner"
    state.space_sqft = 0
    state.recommended_plants = []
    state.saved_plants = []
    return index(state)

set_website_title("Native Plant Finder")
set_site_information(
    author="Klara Hartwell",
    description="Find native plants for your garden based on your region, gardening level, and space.",
    sources="Plant data: bplant.org, \"Ecoregions of North America.\" Map: U.S. EPA, \"Level III and IV Ecoregions of the Continental United States.\"",
    planning=["brainstorm.pdf", "design.pdf"],
    links=["https://github.com/klarahartwell/native_plant_finder"]
)
hide_debug_information()
set_website_framed(False)

start_server(State("", "beginner", 0, [], []))
