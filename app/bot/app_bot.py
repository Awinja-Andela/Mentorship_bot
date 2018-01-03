from flask import request, json, jsonify, make_response
from flask_restful import Resource
from app.models.models import Mentor


class MentorBot(Resource):
    def post(self):
        q_name = self.clean_response()
        if q_name:
            if type(q_name) == list:
                name = q_name[0] + " " + q_name[1]
                phone_number = q_name[2]
                stack = q_name[3]
                stack_details = q_name[4]
                email = q_name[5]
                slack_team = q_name[6]
                blog = q_name[7]
                git_profile = q_name[8]
                fb_profile = q_name[9]
                linkedin_profile = q_name[10]
                if name == "" or phone_number == "" or stack == "" or \
                        stack_details == "" or email == "" or slack_team ==\
                        "" or blog == "":
                    return make_response(
                        jsonify({
                            "message": "Fill in all the required fields."
                        }), 201)
                else:
                    check_mentor = Mentor.query.filter_by(
                        contacts=phone_number, stack=stack).first()
                    if check_mentor:
                        return make_response(
                            jsonify({
                                "message": "Sorry mentor with the given number " +
                                phone_number + " and stack "+stack+ " already exists.",
                                "phoneNumber": phone_number
                            }), 201)
                    else:
                        mentor = Mentor(name, phone_number, stack,
                                        stack_details, email, slack_team, blog,
                                        git_profile, fb_profile,
                                        linkedin_profile)
                        mentor.save()
                        return make_response(
                            jsonify({
                                "message": "Thank you for availing yourself as a mentor."
                            }), 200)
            else:
                stack_mentors = []
                mentors_by_stack = Mentor.query.filter_by(stack=q_name).all()
                if mentors_by_stack:
                    for mentors in mentors_by_stack:
                        stack_mentors.append(
                            {
                                "name": mentors.full_name,
                                "git profile": mentors.gitprofile,
                                "linkedin profile": mentors.linkedinprofile,
                                "phone number": mentors.contacts,
                                "email": mentors.email
                            })
                    return make_response(
                        jsonify({
                            "mentors for stack " + q_name: stack_mentors
                        }), 200)
                else:
                    return make_response(
                        jsonify(
                            {
                                'message': "There are no mentors in stack "
                                + q_name
                            }
                        ), 404)
        else:
            return make_response(
                jsonify({
                    "message": "oops sorry incomplete request."
                }), 401)

    def get(self):
        mentors = []
        all_mentors = Mentor.query.all()
        if all_mentors:
            for mentor in all_mentors:
                mentors.append({
                    "name": mentor.full_name,
                    "git profile": mentor.gitprofile,
                    "linkedin profile": mentor.linkedinprofile,
                    "phone number": mentor.contacts,
                    "email": mentor.email

                })
            return make_response(
                jsonify({
                    "all mentors": mentors
                }), 200)
        else:
            return make_response(
                jsonify(
                    {
                        'message': "There are no mentors available."
                    }
                ), 404)

    def clean_response(self):
        payload = request.get_data()
        print("----payload", payload)
        data = json.loads(payload)
        print("----data", data)
        if data['result']['action'] == '@searches':
            return data['result']['parameters']['searches']
        elif data['result']['action'] == '@mentor_details':
            return data['result']['parameters']['mentor_details']
        else:
            return None, 404


class MentorsByStack(Resource):
    """Gets mentors by the stack they specialize in."""

    def get(self, stack):
        stack_mentors = []
        mentors_by_stack = Mentor.query.filter_by(stack=stack).all()
        if mentors_by_stack:
            for mentors in mentors_by_stack:
                stack_mentors.append(
                    {
                        "name": mentors.full_name,
                        "git profile": mentors.gitprofile,
                        "linkedin profile": mentors.linkedinprofile,
                        "phone number": mentors.contacts,
                        "email": mentors.email
                    })
            return make_response(
                jsonify({
                    "mentors for stack " + stack: stack_mentors
                }), 200)
        else:
            return make_response(
                jsonify(
                    {
                        'message': "There are no mentors in the stack" + stack
                    }
                ), 404)
