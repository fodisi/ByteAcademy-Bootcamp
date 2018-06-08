def titlecase(title, exceptions):
#    copy_title = title.lower().split(' ')
#    for x in range(len(copy_title)):
#        if x == 0 or copy_title[x].lower() not in exceptions:
#            copy_title[x] = copy_title[x].title()
#    return ' '.join(copy_title)
    lower_title = title.lower().split(' ')
    new_title = [lower_title[x].title() if (x == 0 or lower_title[x] not in exceptions) else lower_title[x] for x in range(len(lower_title))]
	return ' '.join(new_title)


print(titlecase('the quick brown fox jumps over the lazy dog', ['jumps', 'the', 'over']))
print(titlecase('THE vitamins ARE IN my fresh CALIFORNIA raisins', ['are', 'is', 'in', 'your', 'my']))