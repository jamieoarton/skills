# Add Guest To Folder

Share a Folder with a guest. \
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
    "/v2/folder/{folder_id}/guest/{guest_id}": {
      "post": {
        "summary": "Add Guest To Folder",
        "tags": [
          "Guests"
        ],
        "description": "Share a Folder with a guest. \\\n \\\n***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*",
        "operationId": "AddGuestToFolder",
        "parameters": [
          {
            "name": "folder_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                1057
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
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "AddGuestToFolderrequest",
                "required": [
                  "permission_level"
                ],
                "type": "object",
                "properties": {
                  "permission_level": {
                    "description": "Can be `read` (view only), `comment`, `edit`, or `create` (full).",
                    "type": "string"
                  }
                },
                "examples": [
                  {
                    "permission_level": "read"
                  }
                ]
              },
              "example": {
                "permission_level": "read"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "AddGuestToFolderresponse",
                  "required": [
                    "guest"
                  ],
                  "type": "object",
                  "properties": {
                    "guest": {
                      "title": "Guest5",
                      "required": [
                        "user",
                        "invited_by",
                        "can_see_time_spent",
                        "can_see_time_estimated",
                        "can_edit_tags",
                        "shared"
                      ],
                      "type": "object",
                      "properties": {
                        "user": {
                          "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D~1guest~1%7Bguest_id%7D/post/responses/200/content/application~1json/schema/properties/guest/properties/user"
                        },
                        "invited_by": {
                          "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1user~1%7Buser_id%7D/get/responses/200/content/application~1json/schema/properties/member/properties/invited_by"
                        },
                        "can_see_time_spent": {
                          "type": "boolean"
                        },
                        "can_see_time_estimated": {
                          "type": "boolean"
                        },
                        "can_edit_tags": {
                          "type": "boolean"
                        },
                        "shared": {
                          "title": "Shared5",
                          "required": [
                            "tasks",
                            "lists",
                            "folders"
                          ],
                          "type": "object",
                          "properties": {
                            "tasks": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              },
                              "description": ""
                            },
                            "lists": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              },
                              "description": ""
                            },
                            "folders": {
                              "type": "array",
                              "items": {
                                "title": "Folder4",
                                "required": [
                                  "id",
                                  "name",
                                  "orderindex",
                                  "override_statuses",
                                  "hidden",
                                  "task_count",
                                  "archived",
                                  "statuses",
                                  "lists",
                                  "permission_level"
                                ],
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "type": "string"
                                  },
                                  "name": {
                                    "type": "string"
                                  },
                                  "orderindex": {
                                    "type": "integer",
                                    "contentEncoding": "int32"
                                  },
                                  "override_statuses": {
                                    "type": "boolean"
                                  },
                                  "hidden": {
                                    "type": "boolean"
                                  },
                                  "task_count": {
                                    "type": "string"
                                  },
                                  "archived": {
                                    "type": "boolean"
                                  },
                                  "statuses": {
                                    "type": "array",
                                    "items": {
                                      "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                                    },
                                    "description": ""
                                  },
                                  "lists": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "description": ""
                                  },
                                  "permission_level": {
                                    "type": "string"
                                  }
                                },
                                "examples": [
                                  {
                                    "id": "1057",
                                    "name": "Folder Name",
                                    "orderindex": 5,
                                    "override_statuses": true,
                                    "hidden": false,
                                    "task_count": "20",
                                    "archived": false,
                                    "statuses": [
                                      {
                                        "status": "Open",
                                        "orderindex": 0,
                                        "color": "#d3d3d3",
                                        "type": "open"
                                      },
                                      {
                                        "status": "Closed",
                                        "orderindex": 5,
                                        "color": "#6bc950",
                                        "type": "closed"
                                      }
                                    ],
                                    "lists": [],
                                    "permission_level": "read"
                                  }
                                ]
                              },
                              "description": ""
                            }
                          },
                          "examples": [
                            {
                              "tasks": [],
                              "lists": [],
                              "folders": [
                                {
                                  "id": "1057",
                                  "name": "Folder Name",
                                  "orderindex": 5,
                                  "override_statuses": true,
                                  "hidden": false,
                                  "task_count": "20",
                                  "archived": false,
                                  "statuses": [
                                    {
                                      "status": "Open",
                                      "orderindex": 0,
                                      "color": "#d3d3d3",
                                      "type": "open"
                                    },
                                    {
                                      "status": "Closed",
                                      "orderindex": 5,
                                      "color": "#6bc950",
                                      "type": "closed"
                                    }
                                  ],
                                  "lists": [],
                                  "permission_level": "read"
                                }
                              ]
                            }
                          ]
                        }
                      },
                      "examples": [
                        {
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
                            "folders": [
                              {
                                "id": "1057",
                                "name": "Folder Name",
                                "orderindex": 5,
                                "override_statuses": true,
                                "hidden": false,
                                "task_count": "20",
                                "archived": false,
                                "statuses": [
                                  {
                                    "status": "Open",
                                    "orderindex": 0,
                                    "color": "#d3d3d3",
                                    "type": "open"
                                  },
                                  {
                                    "status": "Closed",
                                    "orderindex": 5,
                                    "color": "#6bc950",
                                    "type": "closed"
                                  }
                                ],
                                "lists": [],
                                "permission_level": "read"
                              }
                            ]
                          }
                        }
                      ]
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
                          "folders": [
                            {
                              "id": "1057",
                              "name": "Folder Name",
                              "orderindex": 5,
                              "override_statuses": true,
                              "hidden": false,
                              "task_count": "20",
                              "archived": false,
                              "statuses": [
                                {
                                  "status": "Open",
                                  "orderindex": 0,
                                  "color": "#d3d3d3",
                                  "type": "open"
                                },
                                {
                                  "status": "Closed",
                                  "orderindex": 5,
                                  "color": "#6bc950",
                                  "type": "closed"
                                }
                              ],
                              "lists": [],
                              "permission_level": "read"
                            }
                          ]
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
                      "folders": [
                        {
                          "id": "1057",
                          "name": "Folder Name",
                          "orderindex": 5,
                          "override_statuses": true,
                          "hidden": false,
                          "task_count": "20",
                          "archived": false,
                          "statuses": [
                            {
                              "status": "Open",
                              "orderindex": 0,
                              "color": "#d3d3d3",
                              "type": "open"
                            },
                            {
                              "status": "Closed",
                              "orderindex": 5,
                              "color": "#6bc950",
                              "type": "closed"
                            }
                          ],
                          "lists": [],
                          "permission_level": "read"
                        }
                      ]
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