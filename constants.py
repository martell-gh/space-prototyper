COMPONENT_TYPES = ["Empty", "MeleeWeapon", "Tag", "Wieldable", "Clothing", "TilePrying", "Item", "UseDelay",
                   "PointLight", "Appearance", "Sprite", "EnergySword", "DisarmMalus", "ToggleableLightVisuals"]

COMPONENT_PROPERTIES = [{"MeleeWeapon": ["attackRate", "damage", "soundHit"]},
                            {"damage": ["types"]},
                                {"types":["Blunt", "Slash", "Structural"]},
                            {"soundHit":["path"]},
                        {"Tag": ["tags"]},
                        {"UseDelay":["delay"]},
                        {"PointLight":["netsync", "enabled", "radius", "energy", "color"]},
                        {"Item":["size", "sprite"]},
                        {"Sprite":["sprite","layers","color", 'state']},
                            {"layers":['- state', 'color', 'visible', 'shader', 'map']},
                        {"EnergySword":['litDamageBonus']},
                            {"litDamageBonus":['types']},
                        {"DisarmMalus":["malus"]}]