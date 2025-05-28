CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DO $$
declare 
	group1 uuid = uuid_generate_v4();
    group2 uuid = uuid_generate_v4();
    group3 uuid = uuid_generate_v4();
    group4 uuid = uuid_generate_v4();
    group5 uuid = uuid_generate_v4();
    group6 uuid = uuid_generate_v4();
    group7 uuid = uuid_generate_v4();
    group8 uuid = uuid_generate_v4();
    group9 uuid = uuid_generate_v4();
    group10 uuid = uuid_generate_v4();
	group11 uuid = uuid_generate_v4();
    group12 uuid = uuid_generate_v4();
    group13 uuid = uuid_generate_v4();
    group14 uuid = uuid_generate_v4();
    group15 uuid = uuid_generate_v4();
    group16 uuid = uuid_generate_v4();
    group17 uuid = uuid_generate_v4();
    group18 uuid = uuid_generate_v4();
    group19 uuid = uuid_generate_v4();
    group20 uuid = uuid_generate_v4();
    group21 uuid = uuid_generate_v4();
    group22 uuid = uuid_generate_v4();
    group23 uuid = uuid_generate_v4();

begin
	INSERT INTO offer_tag_groups
	VALUES
	(group1,  'Accessories'),
	(group2,  'Armor'),
	(group3,  'Artifact'),
	(group4,  'City Resources'),
	(group5,  'Consumable'),
	(group6,  'Farmable'),
	(group7,  'Furniture'),
	(group8,  'Gathering Gear'),
	(group9,  'Laborers'),
	(group10, 'Luxury Goods'),
	(group11, 'Magic'),
	(group12, 'Materials'),
	(group13, 'Melee'),
	(group14, 'Mount'),
	(group15, 'Off-Hand'),
	(group16, 'Other'),
	(group17, 'Product'),
	(group18, 'Ranged'),
	(group19, 'Resource'),
	(group20, 'Tomes'),
	(group21, 'Token'),
	(group22, 'Tool'),
	(group23, 'Trophies');

	INSERT INTO offer_tags
	VALUES
	(uuid_generate_v4(), 'Cape', group1),
	(uuid_generate_v4(), 'Cloth Armor', group1),
	(uuid_generate_v4(), 'Leather Armor', group2),
	(uuid_generate_v4(), 'Plate Armor', group2),
	(uuid_generate_v4(), 'Unique Armor', group2),
	(uuid_generate_v4(), 'Armor Artifact', group3),
	(uuid_generate_v4(), 'Magic Artifact', group3),
	(uuid_generate_v4(), 'Melee Artifact', group3),
	(uuid_generate_v4(), 'Beastheart', group4),
	(uuid_generate_v4(), 'Shadowheart', group4),
	(uuid_generate_v4(), 'Mountainheart', group4),
	(uuid_generate_v4(), 'Rockheart', group4),
	(uuid_generate_v4(), 'Treeheart', group4),
	(uuid_generate_v4(), 'Vineheart', group4),
	(uuid_generate_v4(), 'Consumable-Cooked', group5),
	(uuid_generate_v4(), 'Fish', group5),
	(uuid_generate_v4(), 'Fishing Bait', group5),
	(uuid_generate_v4(), 'Victory Emotes', group5),
	(uuid_generate_v4(), 'Consumable-Map', group5),
	(uuid_generate_v4(), 'Consumable-Other', group5),
	(uuid_generate_v4(), 'Potion', group5),
	(uuid_generate_v4(), 'Vanity', group5),
	(uuid_generate_v4(), 'Farable-Animal', group6),
	(uuid_generate_v4(), 'Seed', group6),
	(uuid_generate_v4(), 'Banner', group7),
	(uuid_generate_v4(), 'Bed', group7),
	(uuid_generate_v4(), 'Chest', group7),
	(uuid_generate_v4(), 'Decoration', group7),
	(uuid_generate_v4(), 'Flag', group7),
	(uuid_generate_v4(), 'Heretic', group7),
	(uuid_generate_v4(), 'Keeper', group7),
	(uuid_generate_v4(), 'Morgana', group7),
	(uuid_generate_v4(), 'Repair Kit', group7),
	(uuid_generate_v4(), 'Table', group7),
	(uuid_generate_v4(), 'Unique', group7),
	(uuid_generate_v4(), 'Harvester', group8),
	(uuid_generate_v4(), 'Gathering-Fisherman', group8),
	(uuid_generate_v4(), 'Skinner', group8),
	(uuid_generate_v4(), 'Miner', group8),
	(uuid_generate_v4(), 'Quarrier', group8),
	(uuid_generate_v4(), 'Gathering-Lumberjack', group8),
	(uuid_generate_v4(), 'Cropper', group9),
	(uuid_generate_v4(), 'Laborers-Fisherman', group9),
	(uuid_generate_v4(), 'Gamekeeper', group9),
	(uuid_generate_v4(), 'Fletcher', group9),
	(uuid_generate_v4(), 'Imbuer', group9),
	(uuid_generate_v4(), 'Mercenary', group9),
	(uuid_generate_v4(), 'Prospector', group9),
	(uuid_generate_v4(), 'Stonecutter', group9),
	(uuid_generate_v4(), 'Tinker', group9),
	(uuid_generate_v4(), 'Blacksmith', group9),
	(uuid_generate_v4(), 'Laborers-Lumberjack', group9),
	(uuid_generate_v4(), 'Any', group10),
	(uuid_generate_v4(), 'Bridgewatch', group10),
	(uuid_generate_v4(), 'Caerleon', group10),
	(uuid_generate_v4(), 'Fort Sterling', group10),
	(uuid_generate_v4(), 'Lymhurst', group10),
	(uuid_generate_v4(), 'Martlock', group10),
	(uuid_generate_v4(), 'Thetford', group10),
	(uuid_generate_v4(), 'Arcane Staff', group11),
	(uuid_generate_v4(), 'Crused Staff', group11),
	(uuid_generate_v4(), 'Fire Staff', group11),
	(uuid_generate_v4(), 'Frost Staff', group11),
	(uuid_generate_v4(), 'Holy Staff', group11),
	(uuid_generate_v4(), 'Nature Staff', group11),
	(uuid_generate_v4(), 'Shapeshifter Staff', group11),
	(uuid_generate_v4(), 'Essence', group12),
	(uuid_generate_v4(), 'Materials-Other', group12),
	(uuid_generate_v4(), 'Relic', group12),
	(uuid_generate_v4(), 'Rune', group12),
	(uuid_generate_v4(), 'Avalonian Shards', group12),
	(uuid_generate_v4(), 'Crystal Shards', group12),
	(uuid_generate_v4(), 'Soul', group12),
	(uuid_generate_v4(), 'Axe', group13),
	(uuid_generate_v4(), 'Dagger', group13),
	(uuid_generate_v4(), 'Hammer', group13),
	(uuid_generate_v4(), 'War Gloves', group13),
	(uuid_generate_v4(), 'Mace', group13),
	(uuid_generate_v4(), 'Quarterstaff', group13),
	(uuid_generate_v4(), 'Spear', group13),
	(uuid_generate_v4(), 'Sword', group13),
	(uuid_generate_v4(), 'Armored Horse', group14),
	(uuid_generate_v4(), 'Battle Mount', group14),
	(uuid_generate_v4(), 'Swiftclaw', group14),
	(uuid_generate_v4(), 'Direbear', group14),
	(uuid_generate_v4(), 'Direboar', group14),
	(uuid_generate_v4(), 'Direwolf', group14),
	(uuid_generate_v4(), 'Stag or Moose', group14),
	(uuid_generate_v4(), 'Mule', group14),
	(uuid_generate_v4(), 'Ox', group14),
	(uuid_generate_v4(), 'Rare Mount', group14),
	(uuid_generate_v4(), 'Riding Horse', group14),
	(uuid_generate_v4(), 'Swamp Dragon', group14),
	(uuid_generate_v4(), 'Book', group15),
	(uuid_generate_v4(), 'Horn', group15),
	(uuid_generate_v4(), 'Orb', group15),
	(uuid_generate_v4(), 'Shield', group15),
	(uuid_generate_v4(), 'Torch', group15),
	(uuid_generate_v4(), 'Totem', group15),
	(uuid_generate_v4(), 'Hideout Construction Kit', group16),
	(uuid_generate_v4(), 'Product-Animal', group17),
	(uuid_generate_v4(), 'Product-Cooked', group17),
	(uuid_generate_v4(), 'Farming', group17),
	(uuid_generate_v4(), 'Journals', group17),
	(uuid_generate_v4(), 'Bow', group18),
	(uuid_generate_v4(), 'Crossbow', group18),
	(uuid_generate_v4(), 'Cloth', group19),
	(uuid_generate_v4(), 'Fiber', group19),
	(uuid_generate_v4(), 'Hide', group19),
	(uuid_generate_v4(), 'Leather', group19),
	(uuid_generate_v4(), 'Metal Bar', group19),
	(uuid_generate_v4(), 'Ore', group19),
	(uuid_generate_v4(), 'Resource-Other', group19),
	(uuid_generate_v4(), 'Planks', group19),
	(uuid_generate_v4(), 'Stone', group19),
	(uuid_generate_v4(), 'Stone Block', group19),
	(uuid_generate_v4(), 'Wood', group19),
	(uuid_generate_v4(), 'Tome of Insight', group20),
	(uuid_generate_v4(), 'Fiber Harvester Tomes', group20),
	(uuid_generate_v4(), 'Tomes-Animal Skinner Tomes', group20),
	(uuid_generate_v4(), 'Ore Miner Tomes', group20),
	(uuid_generate_v4(), 'Quarrier Tomes', group20),
	(uuid_generate_v4(), 'Lumberjack Tomes', group20),
	(uuid_generate_v4(), 'Arena Sigil', group21),
	(uuid_generate_v4(), 'Crystal League Token', group21),
	(uuid_generate_v4(), 'Event', group21),
	(uuid_generate_v4(), 'Token-Map', group21),
	(uuid_generate_v4(), 'Token-Other', group21),
	(uuid_generate_v4(), 'Royal Sigil', group21),
	(uuid_generate_v4(), 'Siege Hammer', group22),
	(uuid_generate_v4(), 'Fishing Rod', group22),
	(uuid_generate_v4(), 'Pickaxe', group22),
	(uuid_generate_v4(), 'Sickle', group22),
	(uuid_generate_v4(), 'Siege Banner', group22),
	(uuid_generate_v4(), 'Skinning Knife', group22),
	(uuid_generate_v4(), 'Stone Hammer', group22),
	(uuid_generate_v4(), 'Tracking Toolkit', group22),
	(uuid_generate_v4(), 'Wood Axe', group22),
	(uuid_generate_v4(), 'Fiber Trophy', group23),
	(uuid_generate_v4(), 'Fishing Trophy', group23),
	(uuid_generate_v4(), 'General Trophy', group23),
	(uuid_generate_v4(), 'Hide Trophy', group23),
	(uuid_generate_v4(), 'Mercenary Trophy', group23),
	(uuid_generate_v4(), 'Ore Trophy', group23),
	(uuid_generate_v4(), 'Stone Trophy', group23),
	(uuid_generate_v4(), 'Wood Trophy', group23);
	
    INSERT INTO offer_qualities
    VALUES
    (uuid_generate_v4(), 'Normal'),
    (uuid_generate_v4(), 'Good'),
    (uuid_generate_v4(), 'Outstanding'),
    (uuid_generate_v4(), 'Excellent'),
    (uuid_generate_v4(), 'Masterpiece');
    
    INSERT INTO offer_tiers
    VALUES
    (uuid_generate_v4(), 'T1', null),
    (uuid_generate_v4(), 'T2', null),
    (uuid_generate_v4(), 'T3', null),
    (uuid_generate_v4(), 'T4', 4.0),
	(uuid_generate_v4(), 'T4.1', 4.1),
	(uuid_generate_v4(), 'T4.2', 4.2),
	(uuid_generate_v4(), 'T4.3', 4.3),
	(uuid_generate_v4(), 'T4.4', 4.4),
    (uuid_generate_v4(), 'T5', 5.0),
	(uuid_generate_v4(), 'T5.1', 5.1),
	(uuid_generate_v4(), 'T5.2', 5.2),
	(uuid_generate_v4(), 'T5.3', 5.3),
	(uuid_generate_v4(), 'T5.4', 5.4),
    (uuid_generate_v4(), 'T6', 6.0),
	(uuid_generate_v4(), 'T6.1', 6.1),
	(uuid_generate_v4(), 'T6.2', 6.2),
	(uuid_generate_v4(), 'T6.3', 6.3),
	(uuid_generate_v4(), 'T6.4', 6.4),
    (uuid_generate_v4(), 'T7', 7.0),
	(uuid_generate_v4(), 'T7.1', 7.1),
	(uuid_generate_v4(), 'T7.2', 7.2),
	(uuid_generate_v4(), 'T7.3', 7.3),
	(uuid_generate_v4(), 'T7.4', 7.4),
    (uuid_generate_v4(), 'T8', 8.0),
	(uuid_generate_v4(), 'T8.1', 8.1),
	(uuid_generate_v4(), 'T8.2', 8.2),
	(uuid_generate_v4(), 'T8.3', 8.3),
	(uuid_generate_v4(), 'T8.4', 8.4);
    
    INSERT INTO roles
    VALUES
    (uuid_generate_v4(), 'user', 1),
    (uuid_generate_v4(), 'moderator', 2),
    (uuid_generate_v4(), 'admin', 3);

end $$;

