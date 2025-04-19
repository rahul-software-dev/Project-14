from flask import request, jsonify
from . import api
from app.db.session import get_db
from app.models.user import User
from app.models.subscription import Subscription
from app.services.billing import extend_subscription
from app.services.churn_predictor import predict_churn_risk

@api.route('/users', methods=['GET'])
def list_users():
    db = next(get_db())
    users = db.query(User).all()
    return jsonify([
        {"id": user.id, "name": user.name, "email": user.email}
        for user in users
    ])

@api.route('/subscriptions', methods=['GET'])
def list_subscriptions():
    db = next(get_db())
    subs = db.query(Subscription).all()
    return jsonify([
        {
            "id": s.id,
            "user_id": s.user_id,
            "status": s.status,
            "start_date": s.start_date.isoformat() if s.start_date else None,
            "end_date": s.end_date.isoformat() if s.end_date else None,
            "auto_renew": s.auto_renew
        }
        for s in subs
    ])

@api.route('/subscription/<int:sub_id>/extend', methods=['POST'])
def extend_sub(sub_id):
    days = request.json.get('days', 30)
    success = extend_subscription(sub_id, days)
    return jsonify({"success": success})

@api.route('/subscription/<int:sub_id>/risk', methods=['GET'])
def get_churn_risk(sub_id):
    db = next(get_db())
    sub = db.query(Subscription).filter_by(id=sub_id).first()
    if not sub:
        return jsonify({"error": "Subscription not found"}), 404

    risk = predict_churn_risk(sub)
    return jsonify({
        "subscription_id": sub.id,
        "churn_risk_score": round(risk, 3)
    })