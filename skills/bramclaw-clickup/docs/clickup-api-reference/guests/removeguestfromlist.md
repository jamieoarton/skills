# Remove Guest From List

Revoke a guest's access to a List.\
 \
***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/list/{list_id}/guest/{guest_id}": {
      "delete": {
        "summary": "Remove Guest From List",
        "tags": [
          "Guests"
        ],
        "description": "Revoke a guest's access to a List.\\\n \\\n***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*",
        "operationId": "RemoveGuestFromList",
        "parameters": [
          {
            "name": "list_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                1427
              ]
            }
          },
          {
            "name": "guest_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                403
              ]
            }
          },
          {
            "name": "include_shared",
            "in": "query",
            "description": "Exclude details of items shared with the guest by setting this parameter to `false`. By default this parameter is set to `true`.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                false
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "RemoveGuestFromListresponse",
                  "required": [
                    "guest"
                  ],
                  "type": "object",
                  "properties": {
                    "guest": {
                      "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D~1guest~1%7Bguest_id%7D/delete/responses/200/content/application~1json/schema/properties/guest"
                    }
                  },
                  "examples": [
                    {
                      "guest": {
                        "user": {
                          "id": 184,
                          "username": null,
                          "email": "guest@example.com",
                          "color": null,
                          "profilePicture": null,
                          "initials": "G",
                          "role": 4,
                          "last_active": null,
                          "date_joined": null,
                          "date_invited": "1583358383412"
                        },
                        "invited_by": {
                          "id": 183,
                          "color": "#827718",
                          "username": "Jerry",
                          "email": "jerry@example.com",
                          "initials": "J",
                          "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                        },
                        "can_see_time_spent": true,
                        "can_see_time_estimated": true,
                        "can_edit_tags": true,
                        "shared": {
                          "tasks": [],
                          "lists": [],
                          "folders": []
                        }
                      }
                    }
                  ]
                },
                "example": {
                  "guest": {
                    "user": {
                      "id": 184,
                      "username": null,
                      "email": "guest@example.com",
                      "color": null,
                      "profilePicture": null,
                      "initials": "G",
                      "role": 4,
                      "last_active": null,
                      "date_joined": null,
                      "date_invited": "1583358383412"
                    },
                    "invited_by": {
                      "id": 183,
                      "color": "#827718",
                      "username": "Jerry",
                      "email": "jerry@example.com",
                      "initials": "J",
                      "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                    },
                    "can_see_time_spent": true,
                    "can_see_time_estimated": true,
                    "can_edit_tags": true,
                    "shared": {
                      "tasks": [],
                      "lists": [],
                      "folders": []
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Guests"
    }
  ]
}
```