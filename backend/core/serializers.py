from builtins import object

class CoreSerializer(object):
    def __init__(self, body):
        self.body = body

    @property
    def users(self):
        output = {'users': []}

        for user in self.body:
            user_details = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'middle_name': user.middle_name,
                'phone_number': user.phone_number, 
                'address': user.address, 
                'state': user.state, 
                'zip_code': user.zip_code,
                'city': user.city,
                'email': user.email,
                'admin': user.admin,
            }
            output['users'].append(user_details)

        return output

    @property
    def quotes(self):
        output = {'quotes': []}

        for quote in self.body:
            quote_details = {
                'id': quote.id,
                'date_submitted': quote.date_submitted,
                'start_date_requested': quote.start_date_requested,
                'end_date_requested': quote.end_date_requested,
                'quoted_price': quote.quoted_price,
                'final_cost': quote.final_cost,
                'completed': quote.completed,
                'accepted': quote.accepted,
                'user': quote.user.id,
            }
            output['quotes'].append(quote_details)

        return output