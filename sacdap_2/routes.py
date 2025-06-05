from flask import render_template, request, redirect, url_for, flash
from app import app
from forms import EnrollmentForm, ContactForm
from data import courses_data, add_enrollment, add_contact, get_course_by_id, get_all_courses_for_search
import logging

@app.route('/')
def home():
    """Homepage showing all course categories"""
    search_courses = get_all_courses_for_search()
    return render_template('home.html', courses_data=courses_data, search_courses=search_courses)

@app.route('/stock-market')
def stock_market():
    """Stock market courses page"""
    search_courses = get_all_courses_for_search()
    return render_template('stock_market.html', 
                         courses=courses_data['stock_market'], 
                         search_courses=search_courses)

@app.route('/it-courses')
def it_courses():
    """IT courses page"""
    search_courses = get_all_courses_for_search()
    return render_template('it_courses.html', 
                         courses=courses_data['it'], 
                         search_courses=search_courses)

@app.route('/accounts')
def accounts():
    """Accounts courses page"""
    search_courses = get_all_courses_for_search()
    return render_template('accounts.html', 
                         courses=courses_data['accounting'], 
                         search_courses=search_courses)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form"""
    search_courses = get_all_courses_for_search()
    form = ContactForm()
    
    if form.validate_on_submit():
        try:
            contact_data = {
                'name': form.name.data,
                'email': form.email.data,
                'subject': form.subject.data,
                'message': form.message.data
            }
            
            contact_id = add_contact(contact_data)
            logging.info(f"New contact message received: {contact_id}")
            
            flash('Thank you for your message! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
            
        except Exception as e:
            logging.error(f"Error processing contact form: {str(e)}")
            flash('There was an error processing your message. Please try again.', 'error')
    
    return render_template('contact.html', form=form, search_courses=search_courses)

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    """Common enrollment page for all courses"""
    search_courses = get_all_courses_for_search()
    form = EnrollmentForm()
    
    # Pre-select course if coming from a specific course page
    course_id = request.args.get('course')
    if course_id and request.method == 'GET':
        form.course_interested.data = course_id
    
    if form.validate_on_submit():
        try:
            enrollment_data = {
                'name': form.name.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'course_interested': form.course_interested.data,
                'message': form.message.data
            }
            
            enrollment_id = add_enrollment(enrollment_data)
            logging.info(f"New enrollment received: {enrollment_id}")
            
            # Get course details for success page
            course = get_course_by_id(form.course_interested.data)
            course_name = course['name'] if course else 'Selected Course'
            
            return render_template('success.html', 
                                 course_name=course_name,
                                 student_name=form.name.data,
                                 search_courses=search_courses)
            
        except Exception as e:
            logging.error(f"Error processing enrollment: {str(e)}")
            flash('There was an error processing your enrollment. Please try again.', 'error')
    
    return render_template('enrollment.html', form=form, search_courses=search_courses)

@app.route('/search')
def search_course():
    """Handle course search from dropdown"""
    course_id = request.args.get('course')
    if not course_id:
        flash('Please select a course to search.', 'warning')
        return redirect(url_for('home'))
    
    # Redirect to enrollment page with pre-selected course
    return redirect(url_for('enroll', course=course_id))

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    search_courses = get_all_courses_for_search()
    return render_template('base.html', search_courses=search_courses), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    search_courses = get_all_courses_for_search()
    return render_template('base.html', search_courses=search_courses), 500
