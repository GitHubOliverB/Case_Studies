#!/usr/bin/python

"""
Summary:

Define all the features you want to use in the Feature_List. 
They must be present in all dataframes. Only takes strings.


Feature_List = ['age', 'height_in_cm', 'size', 'weight_in_kg',
       'price', 'category_Shirts casual', 'category_bad', 'category_good',
       'category_medium', 'product_group_bad', 'product_group_good',
       'product_group_medium', 'color_Blue', 'color_bad', 'color_good',
       'color_medium', 'brand_Brand2', 'brand_bad', 'brand_good',
       'brand_medium', 'shipping_country_0', 'shipping_country_1',
       'shipping_country_2', 'shipping_country_3', 'shipping_country_4',
       'shipping_country_5', 'shipping_country_6', 'shipping_country_7']
				
"""
Feature_List = ['age', 'height_in_cm', 'size', 'shipping_country', 'weight_in_kg', 
				'price', 'category_Belts', 'category_Blazers', 'category_Coats', 'category_Jackets', 
				'category_Knitted tops', 'category_Leather Jackets', 'category_Pants', 'category_Shirt short sleeves', 
				'category_Shirts business', 'category_Shirts casual', 'category_Shorts', 'category_Sweaters', 'category_T-Shirts', 
				'category_Underwear', 'category_Vest', 'product_group_Belt casual', 'product_group_Blazer Knit', 
				'product_group_Blazer casual', 'product_group_Blouson', 'product_group_Boxers', 'product_group_Briefs', 
				'product_group_Business shirt short sleeves', 'product_group_C-Neck', 'product_group_Caban', 
				'product_group_Cardigan', 'product_group_Cargo Shorts', 'product_group_Casual shirt short sleeves', 
				'product_group_Chino regular fit', 'product_group_Chino shorts', 'product_group_Chino slim fit', 
				'product_group_Cloth pants', 'product_group_Denim jacket', 'product_group_Down jacket', 
				'product_group_Field jacket', 'product_group_Functional jacket', 'product_group_Hoodie', 
				'product_group_Indoor Vest', 'product_group_Jeans shorts', 'product_group_Leather Jacket', 
				'product_group_Light coat', 'product_group_Light jacket', 'product_group_Medium fit', 'product_group_Outdoor Vest', 
				'product_group_PU-Jacket', 'product_group_Parka', 'product_group_Polo shirt longsleeves', 
				'product_group_Polo shirt shortsleeves', 'product_group_Regular fit', 'product_group_Short Coat', 
				'product_group_Slim fit', 'product_group_Sweat jacket', 'product_group_Sweatpants', 'product_group_Sweatshirt', 
				'product_group_Swim shorts', 'product_group_T-shirt Basic', 'product_group_T-shirt Print', 
				'product_group_T-shirt long sleeves', 'product_group_T-shirt striped / patterned', 'product_group_Trench coat', 
				'product_group_Troyer', 'product_group_Trunks', 'product_group_Turtle neck', 'product_group_Undershirt', 
				'product_group_V-Neck', 'product_group_Winter coat', 'product_group_Winter jacket', 'color_Beige', 'color_Black', 
				'color_Blue', 'color_Brown', 'color_Green', 'color_Grey', 'color_Metal', 'color_Multicolor', 'color_Orange', 
				'color_Pink', 'color_Red', 'color_Turquoise', 'color_Violet', 'color_White', 'color_Yellow', 'brand_Brand0', 
				'brand_Brand1', 'brand_Brand10', 'brand_Brand11', 'brand_Brand12', 'brand_Brand13', 'brand_Brand14', 
				'brand_Brand15', 'brand_Brand16', 'brand_Brand17', 'brand_Brand18', 'brand_Brand19', 'brand_Brand2', 
				'brand_Brand20', 'brand_Brand21', 'brand_Brand22', 'brand_Brand23', 'brand_Brand24', 'brand_Brand25', 
				'brand_Brand26', 'brand_Brand27', 'brand_Brand28', 'brand_Brand29', 'brand_Brand3', 'brand_Brand30', 
				'brand_Brand31', 'brand_Brand32', 'brand_Brand33', 'brand_Brand34', 'brand_Brand35', 'brand_Brand37', 
				'brand_Brand38', 'brand_Brand39', 'brand_Brand4', 'brand_Brand40', 'brand_Brand41', 'brand_Brand42', 
				'brand_Brand43', 'brand_Brand44', 'brand_Brand45', 'brand_Brand46', 'brand_Brand47', 'brand_Brand48', 
				'brand_Brand49', 'brand_Brand5', 'brand_Brand50', 'brand_Brand51', 'brand_Brand52', 'brand_Brand53', 
				'brand_Brand54', 'brand_Brand55', 'brand_Brand56', 'brand_Brand57', 'brand_Brand58', 'brand_Brand59', 
				'brand_Brand6', 'brand_Brand60', 'brand_Brand61', 'brand_Brand62', 'brand_Brand63', 'brand_Brand64', 
				'brand_Brand65', 'brand_Brand66', 'brand_Brand67', 'brand_Brand68', 'brand_Brand69', 'brand_Brand7', 
				'brand_Brand70', 'brand_Brand71', 'brand_Brand72', 'brand_Brand74', 'brand_Brand75', 'brand_Brand76', 
				'brand_Brand77', 'brand_Brand78', 'brand_Brand79', 'brand_Brand8', 'brand_Brand80', 'brand_Brand81', 
				'brand_Brand82', 'brand_Brand83', 'brand_Brand9']