#!/usr/bin/env python3

from ruamel.yaml import YAML

MD = """<!-- generated by index.md.py -->

## [Research and Publications](reviews.html){:.title-image}

"""

yaml = YAML()

def main():
    with open("_data/papers.yaml") as fp:
        data = yaml.load(fp)

    with open("index.md", "w") as fp:
        print(MD, file=fp)
        for paper in data["papers"]:
            title = f'**{paper["title"]}**'
            if "title_image" in paper:
                title = f'[{title}]({paper["title_image"]}){{:.title-image}}'
            fp.write(title)
            if paper.get("links"):
                links = ""
                for link in paper["links"]:
                    (key, val) ,= link.items()
                    key = key.replace("_newtab", "")
                    if key.startswith("("):
                        links += " &middot; "
                    else:
                        links += " \\| "
                    links += f'[{key}]({val}){{:target="blank"}}'
                links = links[4:]
                fp.write(f' &nbsp; [ {links} ]')
            fp.write("\\\n")
            fp.write(", ".join(paper.get("authors", [])))
            fp.write("\\\n")
            venue = paper.get("venue", "")
            venue = venue.replace("'", "\\'")
            longvenue = paper.get("longvenue", "")
            venuelink = paper.get("venue_link", "#")
            if not longvenue:
                venue = f'<span class="no-fullvenue">{venue}</span>'
            else:
                venue = f'[{venue}]({venuelink}){{:.hover-over title="{longvenue}"}}'
            fp.write(venue)
            fp.write("\n\n")

if __name__ == "__main__":
    main()
