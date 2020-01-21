
password_1 = input('請輸入密碼(你一共有三次機會): ')
if password_1 == 'a123456':
	print('登入成功')
	
else:
	print('密碼錯誤', '你還有兩次機會')
	if True:
		password_2 = input('請輸入密碼: ')
		if password_1 == 'a123456':
			print('登入成功')
			
		else:
			print('密碼錯誤', '你還有一次機會')
			if True:
				password_3 = input('請輸入密碼: ')
				if password_3 == 'a123456':
					print('登入成功')
					
				else:
					print('無法輸入密碼')
					


	
