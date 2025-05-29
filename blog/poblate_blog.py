from .models import *
from django.utils import timezone

"""
Script per poblar el blog amb dades fictícies.

Crea publicacions de prova, autors i etiquetes per facilitar el desenvolupament i proves.
"""

#Crear autors
authors = [
    Author.objects.create(first_name="Marc", last_name="Gamer", email="marc.gamer@vgameblog.com"),
    Author.objects.create(first_name="Laura", last_name="Pixel", email="laura.pixel@nextgennews.com"),
    Author.objects.create(first_name="Joel", last_name="Spawn", email="joel.spawn@controllerhub.net"),
    Author.objects.create(first_name="Elena", last_name="Quest", email="elena.quest@gamerszone.com"),
    Author.objects.create(first_name="Toni", last_name="Loot", email="toni.loot@indiexplore.org"),
]

#Crear tags
tags = {
    "RPG": Tag.objects.create(caption="RPG"),
    "Multiplayer": Tag.objects.create(caption="Multiplayer"),
    "Retro": Tag.objects.create(caption="Retro"),
    "Indie": Tag.objects.create(caption="Indie"),
    "E-Sports": Tag.objects.create(caption="E-Sports"),
    "Shooter": Tag.objects.create(caption="Shooter"),
    "Survival": Tag.objects.create(caption="Survival"),
}

#Crear posts
post_data = [
    ("Top 10 RPGs del 2025", "Els RPGs que no et pots perdre", "rpg_top_2025.jpg", "top-rpgs-2025", ["RPG"]),
    ("Els millors jocs multijugador actuals", "Connecta i juga amb amics", "top_multiplayer.jpg", "top-multiplayer-2025", ["Multiplayer"]),
    ("Clàssics retro que tornen", "Els millors remakes del moment", "retro_hits.jpg", "retro-remakes", ["Retro"]),
    ("Les joies indie que han captivat tothom", "Creativitat i passió en píxels", "indie_gems.jpg", "indie-hits", ["Indie"]),
    ("Campionats E-Sports del 2025", "Tot el que necessites saber", "esports_events.jpg", "esports-2025", ["E-Sports"]),
    ("Shooter de nova generació", "Adrenalina i gràfics de pel·lícula", "nextgen_shooters.jpg", "nextgen-shooters", ["Shooter"]),
    ("Sobreviure al postapocalipsi", "Els millors jocs de supervivència", "survival_guide.jpg", "survival-games", ["Survival"]),
    ("Evolució dels controls en jocs retro", "Com ha canviat la manera de jugar", "controls_retro.jpg", "retro-controls", ["Retro"]),
    ("Tendències del disseny indie", "Art visual i narrativa alternativa", "indie_design.jpg", "indie-trends", ["Indie"]),
    ("Top jocs en línia free-to-play", "Diversió sense gastar ni un duro", "free_to_play.jpg", "free-multiplayer", ["Multiplayer"]),
    ("Els RPGs més originals de l'any", "Històries que deixen petjada", "unique_rpgs.jpg", "original-rpgs-2025", ["RPG", "Indie"]),
    ("Els millors moments E-Sports 2024", "Jugada mestra!", "esports_moments.jpg", "esports-2024-top", ["E-Sports"]),
    ("Nova onada de shooters tàctics", "Pensa abans de disparar", "tactical_shooters.jpg", "tactical-shooters", ["Shooter"]),
    ("La narrativa en jocs survival", "Quan sobreviure també és emocionar-se", "survival_story.jpg", "narrative-survival", ["Survival", "Indie"]),
    ("L'art del píxel torna amb força", "Gràfics retro en ple segle XXI", "pixel_art.jpg", "pixel-art-revival", ["Retro", "Indie"]),
]

for i, (title, excerpt, image, slug, tag_list) in enumerate(post_data):
    post = Post.objects.create(
        title=title,
        excerpt=excerpt,
        image=image,
        date=timezone.now(),
        slug=slug,
        content=f"Contingut extens del post '{title}', parlant sobre {', '.join(tag_list)}.",
        author=authors[i % len(authors)]
    )
    post.tags.set([tags[tag] for tag in tag_list])