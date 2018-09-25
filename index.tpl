<h1>Verkefni 4 - API</h1>

% for i in data['results']:
	<h3>{{i['longName']}}</h3>
	<h4>{{i['shortName']}}</h4>
	<h3>{{i['value']}}</h3>
% end