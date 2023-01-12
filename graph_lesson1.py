# solving the Konigsberg Bridge Problem 
# representing walks in the city 

# "CcAaBbAdgDeA"
# make a list to represent the 7 bridges
BRIDGES = [
    "AaB",
    "AbB",
    "AcC",
    "AdC",
    "AeD",
    "BfD",
    "CgD",
]


def get_walks_starting_from (area, bridges=BRIDGES):
    walks=[]

    def make_walks(area, walked=None, bridges_crossed=None):
        walked = walked or area
        bridges_crossed = bridges_crossed or ()
        # Get all of the bridges conencted to 'area'
        # that haven't been crossed
        available_bridges = [
            bridge
            for bridge in bridges
            if area in bridge and bridge not in bridges_crossed
        ]

        # Determine if the wlak has ended
        if not available_bridges:
            walks.append(walked)
        
        # Walk the bridge to the adjacent area and recurse 
        for bridge in available_bridges:
            crossing = bridge[1:] if bridge [0] == area else bridge [1:: -1]
            make_walks(
                area = crossing [-1],
                walked = walked +crossing,
                bridges_crossed = (bridge, *bridges_crossed),
            )

    make_walks(area)
    return walks

walks_starting_from = {area: get_walks_starting_from(area) for area in "ABCD"}
num_total_walks = sum(len(walks) for walks in walks_starting_from.values())
print(num_total_walks)