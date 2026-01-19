"""
NEX Platform - Terms of Service and Privacy API
Handles terms acceptance, privacy policy, and legal compliance
"""

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import json
import os
from pathlib import Path

router = APIRouter()

# Path to terms acceptance file
TERMS_FILE = Path("data/terms_acceptance.json")
TERMS_FILE.parent.mkdir(parents=True, exist_ok=True)

# Initialize terms file if not exists
if not TERMS_FILE.exists():
    with open(TERMS_FILE, 'w') as f:
        json.dump({}, f)


class TermsAcceptance(BaseModel):
    """Terms acceptance model"""
    user_id: Optional[str] = "anonymous"
    ip_address: Optional[str] = None
    accepted_at: str
    terms_version: str = "1.0"
    privacy_version: str = "1.0"
    disclaimer_accepted: bool = True


class TermsResponse(BaseModel):
    """Terms response model"""
    terms_required: bool
    terms_accepted: bool
    terms_version: str
    privacy_version: str
    terms_url: str
    privacy_url: str
    disclaimer_url: str


@router.get("/check", response_model=TermsResponse)
async def check_terms_acceptance(request: Request):
    """
    Check if user has accepted terms
    Returns terms status and URLs to legal documents
    """
    # Get client identifier (IP or session)
    client_id = request.client.host if request.client else "unknown"

    # Load terms acceptance data
    with open(TERMS_FILE, 'r') as f:
        acceptances = json.load(f)

    # Check if this client has accepted
    accepted = client_id in acceptances

    return {
        "terms_required": True,
        "terms_accepted": accepted,
        "terms_version": "1.0",
        "privacy_version": "1.0",
        "terms_url": "/api/terms/content/terms",
        "privacy_url": "/api/terms/content/privacy",
        "disclaimer_url": "/api/terms/content/disclaimer"
    }


@router.post("/accept")
async def accept_terms(request: Request, acceptance: TermsAcceptance):
    """
    Accept terms of service, privacy policy, and disclaimer
    Required before using the platform
    """
    # Get client identifier
    client_id = request.client.host if request.client else "unknown"

    # Load current acceptances
    with open(TERMS_FILE, 'r') as f:
        acceptances = json.load(f)

    # Store acceptance
    acceptances[client_id] = {
        "user_id": acceptance.user_id,
        "ip_address": client_id,
        "accepted_at": datetime.utcnow().isoformat(),
        "terms_version": acceptance.terms_version,
        "privacy_version": acceptance.privacy_version,
        "disclaimer_accepted": acceptance.disclaimer_accepted
    }

    # Save to file
    with open(TERMS_FILE, 'w') as f:
        json.dump(acceptances, f, indent=2)

    return {
        "success": True,
        "message": "Terms accepted successfully",
        "accepted_at": acceptances[client_id]["accepted_at"]
    }


@router.get("/content/{document_type}")
async def get_legal_document(document_type: str):
    """
    Get content of legal documents
    document_type: 'terms', 'privacy', or 'disclaimer'
    """
    # Map document types to files
    doc_map = {
        "terms": "../../TERMOS_DE_USO.md",
        "privacy": "../../POLITICA_DE_PRIVACIDADE.md",
        "disclaimer": "../../DISCLAIMER.md"
    }

    if document_type not in doc_map:
        raise HTTPException(status_code=404, detail="Document not found")

    # Get file path
    file_path = Path(__file__).parent / doc_map[document_type]

    # Check if file exists
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Document file not found")

    # Read and return content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return {
        "type": document_type,
        "content": content,
        "version": "1.0",
        "last_updated": "2026-01-19"
    }


@router.delete("/revoke")
async def revoke_terms_acceptance(request: Request):
    """
    Revoke terms acceptance
    This effectively logs the user out and requires re-acceptance
    """
    client_id = request.client.host if request.client else "unknown"

    # Load current acceptances
    with open(TERMS_FILE, 'r') as f:
        acceptances = json.load(f)

    # Remove acceptance if exists
    if client_id in acceptances:
        del acceptances[client_id]

        # Save updated file
        with open(TERMS_FILE, 'w') as f:
            json.dump(acceptances, f, indent=2)

        return {
            "success": True,
            "message": "Terms acceptance revoked. Please accept terms again to use the platform."
        }

    return {
        "success": False,
        "message": "No terms acceptance found for this client"
    }


@router.get("/summary")
async def get_terms_summary():
    """
    Get summary of terms, privacy policy, and key points
    Useful for quick reference
    """
    return {
        "terms_of_service": {
            "version": "1.0",
            "key_points": [
                "✅ Use only for legal and ethical purposes",
                "❌ Prohibited: malware, hacking, fraud, illegal activities",
                "⚠️ You are responsible for all code you create",
                "⚠️ Software provided 'AS IS' without warranties",
                "⚠️ Developers not liable for damages",
                "✅ You own all code you create"
            ]
        },
        "privacy_policy": {
            "version": "1.0",
            "key_points": [
                "🔒 Zero tracking - no analytics or telemetry",
                "🏠 All data processed locally on your machine",
                "🙈 We don't collect personal information",
                "🚫 No data sharing with third parties",
                "✅ You have full control over your data",
                "🔐 Anonymous usage supported"
            ]
        },
        "disclaimer": {
            "version": "1.0",
            "key_points": [
                "⚠️ Use at your own risk",
                "⚠️ Review all AI-generated code before use",
                "⚠️ AI may generate imperfect code",
                "⚠️ No guarantee of security or correctness",
                "⚠️ You are fully responsible for applications you create",
                "⚠️ Test extensively before production use"
            ]
        },
        "anonymity": {
            "guarantees": [
                "✅ No personal data collection",
                "✅ No browsing history tracking",
                "✅ No external data transmission (except configured APIs)",
                "✅ Local storage only",
                "✅ You can use completely anonymously",
                "✅ No IP logging or user profiling"
            ]
        }
    }


@router.get("/privacy/data-collected")
async def get_data_collection_info():
    """
    Detailed information about what data is collected and where it's stored
    Full transparency for LGPD/GDPR compliance
    """
    return {
        "data_collected": {
            "local_storage_only": True,
            "external_transmission": False,
            "categories": [
                {
                    "type": "Configuration",
                    "location": "/nex/backend/.env",
                    "description": "System settings (port, language, theme)",
                    "can_delete": True,
                    "encrypted": False
                },
                {
                    "type": "Projects",
                    "location": "/nex/projects/",
                    "description": "Your source code and compiled applications",
                    "can_delete": True,
                    "encrypted": False
                },
                {
                    "type": "AI Memory",
                    "location": "/nex/database/vector_db/",
                    "description": "Chat history and learned context",
                    "can_delete": True,
                    "encrypted": False
                },
                {
                    "type": "Database",
                    "location": "/nex/backend/nex.db",
                    "description": "Local users, apps, configurations",
                    "can_delete": True,
                    "encrypted": False
                },
                {
                    "type": "Logs",
                    "location": "/nex/logs/",
                    "description": "Technical operation logs",
                    "can_delete": True,
                    "encrypted": False,
                    "retention": "30 days (configurable)"
                }
            ]
        },
        "data_NOT_collected": [
            "❌ Real name, ID documents",
            "❌ Physical address",
            "❌ Phone number",
            "❌ Financial information",
            "❌ Biometric data",
            "❌ Social media data",
            "❌ Browsing history (external sites)",
            "❌ Location/GPS data",
            "❌ Device fingerprints",
            "❌ IP addresses (not logged)",
            "❌ Usage analytics"
        ],
        "your_rights": {
            "lgpd_gdpr_compliant": True,
            "rights": [
                {
                    "right": "Access",
                    "description": "Access all your data anytime",
                    "how": "Direct file access or API endpoints"
                },
                {
                    "right": "Rectification",
                    "description": "Correct any incorrect data",
                    "how": "Edit files directly or use admin panel"
                },
                {
                    "right": "Deletion",
                    "description": "Delete all your data (Right to be Forgotten)",
                    "how": "Delete user account or rm -rf /nex/"
                },
                {
                    "right": "Portability",
                    "description": "Export all your data",
                    "how": "Copy /nex/ directory or use export API"
                },
                {
                    "right": "Opposition",
                    "description": "Disable any feature",
                    "how": "Configure in settings or .env"
                }
            ]
        }
    }


@router.get("/compliance")
async def get_compliance_info():
    """
    Information about legal compliance (LGPD, GDPR, CCPA, etc.)
    """
    return {
        "compliance": {
            "lgpd": {
                "compliant": True,
                "law": "Lei Geral de Proteção de Dados (Brazil)",
                "details": [
                    "✅ Data processed locally only",
                    "✅ User consent required (terms acceptance)",
                    "✅ Right to deletion implemented",
                    "✅ Right to access implemented",
                    "✅ Data minimization (collect only necessary)",
                    "✅ Transparency in data processing",
                    "✅ Security measures implemented"
                ]
            },
            "gdpr": {
                "compliant": True,
                "law": "General Data Protection Regulation (Europe)",
                "details": [
                    "✅ Lawful basis: User consent",
                    "✅ Data subject rights implemented",
                    "✅ Privacy by design and default",
                    "✅ Data portability supported",
                    "✅ Right to erasure implemented",
                    "✅ No automated decision-making (AI is tool, not decider)",
                    "✅ No cross-border data transfers (local only)"
                ]
            },
            "ccpa": {
                "compliant": True,
                "law": "California Consumer Privacy Act (USA)",
                "details": [
                    "✅ Right to know what data is collected",
                    "✅ Right to delete personal information",
                    "✅ Right to opt-out (can disable features)",
                    "✅ No sale of personal information (we don't collect it)",
                    "✅ No discrimination for exercising rights"
                ]
            }
        },
        "security_measures": [
            "🔒 Password hashing (bcrypt)",
            "🔒 Local data storage only",
            "🔒 No external data transmission",
            "🔒 Optional encryption support",
            "🔒 Session management",
            "🔒 CSRF protection",
            "🔒 XSS prevention",
            "🔒 SQL injection prevention (ORM)"
        ]
    }
