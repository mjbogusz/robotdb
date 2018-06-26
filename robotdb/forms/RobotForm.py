from django import forms
from robotdb.models import Robot, Feature

FEATURE_CHOICES = (('y', 'yes',), ('n', 'no',), ('u', 'unknown',))

class RobotFeatureWidget(forms.widgets.RadioSelect):
	template_name = 'widgets/robotFeatureWidget.html'

	def __init__(self, queryset = None, attrs = None, choices = ()):
		self._choices = choices
		self._queryset = queryset
		super(RobotFeatureWidget, self).__init__(attrs, choices)

	def optgroups(self, name, value, attrs = None):
		groups = []
		for index, groupItem in enumerate(self._queryset):
			if groupItem is None:
				continue

			subgroup = []
			subgroupName = groupItem.name

			for subindex, (subvalue, sublabel) in enumerate(self._choices):
				option = self.create_option(
					subgroupName,
					subvalue,
					sublabel,
					False,
					index,
					subindex = subindex,
					attrs = attrs
				)
				subgroup.append(option)
			textInput = self.create_option(
				subgroupName,
				'testValue',
				'label',
				selected = False,
				index = index,
				subindex = subindex + 1,
				attrs = attrs
			)
			textInput['type'] = 'text'
			subgroup.append(textInput)
			groups.append((subgroupName, subgroup, index))
		return groups

class RobotForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea)
	features = forms.ModelMultipleChoiceField(
		queryset = Feature.objects.all(),
		widget = RobotFeatureWidget(
			queryset = Feature.objects.all(),
			attrs = {
				'class': 'robotFeatureSelectInput',
				'label_class': 'robotFeatureSelectInputLabel',
			},
			choices = FEATURE_CHOICES,
		),
		required = False,
	)

	class Meta:
		model = Robot
		exclude = ()
